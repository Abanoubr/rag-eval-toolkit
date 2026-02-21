import click
    import json
    from .evaluator import RAGEvaluator
    from .backends.openai_backend import OpenAIBackend
    from .metrics.faithfulness import FaithfulnessMetric
    from .metrics.relevancy import AnswerRelevancyMetric
    
    @click.group()
    def main():
        """RAG Evaluation Toolkit CLI"""
        pass
    
    @main.command()
    @click.option('--dataset', type=click.Path(exists=True), required=True, help='Path to JSON dataset')
    @click.option('--output', type=click.Path(), default='report.json', help='Output report path')
    def evaluate(dataset, output):
        """Run evaluation on a dataset"""
        with open(dataset, 'r') as f:
            data = json.load(f)
        
        backend = OpenAIBackend()
        evaluator = RAGEvaluator(backend)
        evaluator.add_metric(FaithfulnessMetric())
        evaluator.add_metric(AnswerRelevancyMetric())
        
        click.echo(f"Evaluating {len(data)} items...")
        results = evaluator.evaluate(data)
        
        with open(output, 'w') as f:
            json.dump(results, f, indent=2)
        click.echo(f"Results saved to {output}")
    
    if __name__ == '__main__':
        main()
