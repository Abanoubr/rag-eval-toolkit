import json
    import os
    
    class HTMLReportGenerator:
        def __init__(self, template_path=None):
            if template_path is None:
                self.template_path = os.path.join(os.path.dirname(__file__), 'templates', 'report.html')
            else:
                self.template_path = template_path
    
        def generate(self, results_data: list, output_path: str):
            # Basic implementation - reads template and injects JSON
            with open(self.template_path, 'r') as f:
                template_content = f.read()
                
            html_content = template_content.replace('{{RESULTS_JSON}}', json.dumps(results_data))
            
            with open(output_path, 'w') as f:
                f.write(html_content)
    
