# TODO: Modify this Procfile to fit your needs
web: python chatbot_v20.py

app = 'parkers-chatbot'
primary_region = 'nrt'

[build]
    builder = 'paketobuildpacks/builder:base'
[env]
    PORT = '8080'
[[services]]
    internal_port = 8000
    protocol = "tcp"
    [services.concurrency]
        hard_limit = 25
        soft_limit = 20
        type = "connections"
    [[services.ports]]
        handlers = ["http"]
        port = 80
    [[services.ports]]
        handlers = ["tls", "http"]
        port = 443
[[vm]]
    size = 'shared-cpu-1x'
