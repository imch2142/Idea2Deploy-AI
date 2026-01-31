def deployment_agent_mock(idea):
    return f"""
Deployment Plan for: {idea}
- Containerize with Docker
- Deploy to IBM Cloud / AWS / Heroku
- CI/CD pipeline using GitHub Actions
- Monitor using basic logging
"""