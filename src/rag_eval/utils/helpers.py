import json
    import csv
    from typing import List, Dict, Any
    
    def format_score(score: float) -> str:
        return f"{score:.2%}"
    
    def load_dataset_from_json(filepath: str) -> List[Dict[str, Any]]:
        with open(filepath, "r") as f:
            return json.load(f)
    
    def save_results_to_csv(results: List[Dict[str, Any]], output_path: str) -> None:
        if not results:
            return
        fieldnames = results[0].keys()
        with open(output_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Results saved to {output_path}")
    
