import os
import time
import json
import statistics
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

@dataclass
class ModelPerformanceMetrics:
    model_name: str
    total_queries: int
    avg_response_time: float
    median_response_time: float
    avg_token_generation_rate: float
    task_success_rate: float
    error_rate: float
    total_execution_time: float

class MultiModelBenchmark:
    def __init__(self, models: List[str]):
        """Initialize benchmark with multiple models"""
        self.models = models
        self.clients = {
            "deepseek": OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",
                api_key=os.getenv('NVIDIA_API_KEY')
            ),
            "openai": OpenAI(
                api_key=os.getenv('OPENAI_API_KEY')
            )
        }
        
        # Real-world use case scenarios
        self.scenarios = [
            {
                "name": "Technical Documentation",
                "prompt": "Generate a comprehensive technical documentation for a RESTful API with authentication and rate limiting.",
                "expected_sections": ["Overview", "Authentication", "Endpoints", "Error Handling"]
            },
            {
                "name": "Code Generation",
                "prompt": "Create a Python class for managing a simple task management system with CRUD operations.",
                "expected_components": ["create_task", "update_task", "delete_task", "list_tasks"]
            },
            {
                "name": "Complex Reasoning",
                "prompt": "Analyze the potential economic and social impacts of widespread AI adoption in the next decade.",
                "expected_depth": ["Economic Transformation", "Labor Market Changes", "Ethical Considerations"]
            },
            {
                "name": "Multilingual Translation",
                "prompt": "Translate a complex technical paragraph about quantum computing from English to Mandarin, maintaining technical accuracy.",
                "languages": ["English", "Mandarin"]
            }
        ]
    
    def evaluate_model(self, model_name: str, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a specific model's performance on a scenario"""
        start_time = time.time()
        response_times = []
        success_count = 0
        error_count = 0
        
        try:
            query_start = time.time()
            response = self.clients[model_name].chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": scenario['prompt']}],
                max_tokens=500
            )
            query_end = time.time()
            
            response_time = (query_end - query_start) * 1000  # Convert to milliseconds
            response_times.append(response_time)
            
            # Validate response against scenario expectations
            content = response.choices[0].message.content
            success = self._validate_response(scenario, content)
            
            if success:
                success_count += 1
            else:
                error_count += 1
        
        except Exception as e:
            error_count += 1
            print(f"Error with {model_name}: {e}")
        
        total_time = time.time() - start_time
        
        return {
            "response_times": response_times,
            "success_count": success_count,
            "error_count": error_count,
            "total_time": total_time
        }
    
    def _validate_response(self, scenario: Dict[str, Any], content: str) -> bool:
        """Validate response based on scenario expectations"""
        if "expected_sections" in scenario:
            return all(section.lower() in content.lower() for section in scenario['expected_sections'])
        
        if "expected_components" in scenario:
            return all(component.lower() in content.lower() for component in scenario['expected_components'])
        
        return True
    
    def run_benchmark(self) -> List[ModelPerformanceMetrics]:
        """Run comprehensive benchmarking across models and scenarios"""
        results = []
        
        for model_name in self.models:
            model_results = {
                "response_times": [],
                "success_count": 0,
                "error_count": 0,
                "total_time": 0
            }
            
            for scenario in self.scenarios:
                scenario_result = self.evaluate_model(model_name, scenario)
                
                model_results['response_times'].extend(scenario_result['response_times'])
                model_results['success_count'] += scenario_result['success_count']
                model_results['error_count'] += scenario_result['error_count']
                model_results['total_time'] += scenario_result['total_time']
            
            metrics = ModelPerformanceMetrics(
                model_name=model_name,
                total_queries=len(self.scenarios),
                avg_response_time=statistics.mean(model_results['response_times']) if model_results['response_times'] else 0,
                median_response_time=statistics.median(model_results['response_times']) if model_results['response_times'] else 0,
                avg_token_generation_rate=len(model_results['response_times']) / model_results['total_time'],
                task_success_rate=(model_results['success_count'] / len(self.scenarios)) * 100,
                error_rate=(model_results['error_count'] / len(self.scenarios)) * 100,
                total_execution_time=model_results['total_time']
            )
            
            results.append(metrics)
        
        return results
    
    def generate_report(self, results: List[ModelPerformanceMetrics]) -> None:
        """Generate a comprehensive benchmarking report"""
        report_path = os.path.join(os.getcwd(), 'benchmark_report.json')
        
        with open(report_path, 'w') as f:
            json.dump([asdict(result) for result in results], f, indent=2)
        
        print(f"Benchmark report generated: {report_path}")

def main():
    benchmark = MultiModelBenchmark([
        "deepseek-ai/deepseek-r1",
        "gpt-3.5-turbo"
    ])
    
    results = benchmark.run_benchmark()
    benchmark.generate_report(results)

if __name__ == "__main__":
    main()
