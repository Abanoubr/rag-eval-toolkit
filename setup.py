from setuptools import setup, find_packages
    
    setup(
        name="rag_eval",
        version="0.1.0",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=[
            "openai>=1.0.0",
            "anthropic>=0.3.0",
            "click>=8.0.0",
            "pydantic>=2.0.0"
        ],
        entry_points={
            "console_scripts": [
                "rag-eval=rag_eval.cli:main",
            ],
        },
    )
