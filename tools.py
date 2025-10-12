SAMPLE_TOOLS = [
    # Web & Search Tools
    {"id": "brave_search", "name": "Brave Search", "description": "Search the web using Brave Search API. Returns top results for any query.", "mcp_server": "brave-search", "full_definition": '{"type": "function"}'},
    {"id": "google_search", "name": "Google Search", "description": "Perform Google searches and retrieve top 10 results with snippets and metadata.", "mcp_server": "google", "full_definition": '{"type": "function"}'},
    {"id": "duckduckgo_search", "name": "DuckDuckGo Search", "description": "Privacy-focused web search engine results and instant answers.", "mcp_server": "duckduckgo", "full_definition": '{"type": "function"}'},
    {"id": "bing_search", "name": "Bing Search", "description": "Search using Bing and retrieve results including news and images.", "mcp_server": "bing", "full_definition": '{"type": "function"}'},
    {"id": "wikipedia_search", "name": "Wikipedia Search", "description": "Search Wikipedia articles and retrieve comprehensive information.", "mcp_server": "wikipedia", "full_definition": '{"type": "function"}'},
    {"id": "arxiv_search", "name": "arXiv Paper Search", "description": "Search scientific papers on arXiv by topic, author, or keyword.", "mcp_server": "arxiv", "full_definition": '{"type": "function"}'},
    
    # Code & Development Tools
    {"id": "github_repos", "name": "GitHub Repository Finder", "description": "Search and retrieve GitHub repositories by language, stars, or keywords.", "mcp_server": "github", "full_definition": '{"type": "function"}'},
    {"id": "github_user", "name": "GitHub User Info", "description": "Get information about GitHub users including repos, followers, and activity.", "mcp_server": "github", "full_definition": '{"type": "function"}'},
    {"id": "github_issues", "name": "GitHub Issues Tracker", "description": "Search GitHub issues and pull requests across repositories.", "mcp_server": "github", "full_definition": '{"type": "function"}'},
    {"id": "gitlab_search", "name": "GitLab Repository Search", "description": "Search GitLab projects and retrieve project metadata.", "mcp_server": "gitlab", "full_definition": '{"type": "function"}'},
    {"id": "npm_packages", "name": "NPM Package Registry", "description": "Search NPM packages and retrieve version history and metadata.", "mcp_server": "npm", "full_definition": '{"type": "function"}'},
    {"id": "pypi_packages", "name": "PyPI Package Search", "description": "Search Python packages on PyPI with version info and documentation links.", "mcp_server": "pypi", "full_definition": '{"type": "function"}'},
    {"id": "docker_hub", "name": "Docker Hub Registry", "description": "Search Docker images and retrieve pull information and tags.", "mcp_server": "docker", "full_definition": '{"type": "function"}'},
    {"id": "stack_overflow", "name": "Stack Overflow Search", "description": "Search Stack Overflow questions and answers by topic.", "mcp_server": "stackoverflow", "full_definition": '{"type": "function"}'},
    {"id": "codeowners", "name": "Code Ownership Analyzer", "description": "Analyze code ownership and identify maintainers across repositories.", "mcp_server": "codeowners", "full_definition": '{"type": "function"}'},
    
    # Data & Database Tools
    {"id": "sql_postgres", "name": "PostgreSQL Query", "description": "Execute SQL queries against PostgreSQL databases with parameterized statements.", "mcp_server": "postgres", "full_definition": '{"type": "function"}'},
    {"id": "sql_mysql", "name": "MySQL Query", "description": "Execute SQL queries on MySQL databases.", "mcp_server": "mysql", "full_definition": '{"type": "function"}'},
    {"id": "sql_sqlite", "name": "SQLite Query", "description": "Query SQLite databases and retrieve structured data.", "mcp_server": "sqlite", "full_definition": '{"type": "function"}'},
    {"id": "mongodb", "name": "MongoDB Queries", "description": "Query MongoDB collections and perform aggregations.", "mcp_server": "mongodb", "full_definition": '{"type": "function"}'},
    {"id": "dynamodb", "name": "DynamoDB Query", "description": "Query and scan DynamoDB tables with filtering options.", "mcp_server": "dynamodb", "full_definition": '{"type": "function"}'},
    {"id": "elasticsearch", "name": "Elasticsearch Search", "description": "Perform full-text and structured searches on Elasticsearch indices.", "mcp_server": "elasticsearch", "full_definition": '{"type": "function"}'},
    {"id": "redis", "name": "Redis Cache", "description": "Get, set, and manage data in Redis with TTL support.", "mcp_server": "redis", "full_definition": '{"type": "function"}'},
    {"id": "bigquery", "name": "Google BigQuery", "description": "Run SQL queries on BigQuery datasets and export results.", "mcp_server": "bigquery", "full_definition": '{"type": "function"}'},
    {"id": "snowflake", "name": "Snowflake Database", "description": "Execute queries on Snowflake warehouses and retrieve data.", "mcp_server": "snowflake", "full_definition": '{"type": "function"}'},
    
    # Cloud & Infrastructure Tools
    {"id": "aws_ec2", "name": "AWS EC2 Manager", "description": "List, start, stop, and manage EC2 instances.", "mcp_server": "aws", "full_definition": '{"type": "function"}'},
    {"id": "aws_s3", "name": "AWS S3 Bucket Manager", "description": "List, upload, download files from S3 buckets.", "mcp_server": "aws", "full_definition": '{"type": "function"}'},
    {"id": "aws_lambda", "name": "AWS Lambda Functions", "description": "List, invoke, and manage Lambda functions.", "mcp_server": "aws", "full_definition": '{"type": "function"}'},
    {"id": "gcp_compute", "name": "Google Compute Engine", "description": "Manage GCP VM instances and retrieve metadata.", "mcp_server": "gcp", "full_definition": '{"type": "function"}'},
    {"id": "gcp_storage", "name": "Google Cloud Storage", "description": "Manage GCS buckets and objects.", "mcp_server": "gcp", "full_definition": '{"type": "function"}'},
    {"id": "azure_vms", "name": "Azure Virtual Machines", "description": "Manage Azure VMs and retrieve instance information.", "mcp_server": "azure", "full_definition": '{"type": "function"}'},
    {"id": "kubernetes", "name": "Kubernetes Cluster", "description": "Query and manage Kubernetes clusters, pods, and deployments.", "mcp_server": "kubernetes", "full_definition": '{"type": "function"}'},
    {"id": "docker_compose", "name": "Docker Compose Manager", "description": "Manage Docker Compose services and containers.", "mcp_server": "docker", "full_definition": '{"type": "function"}'},
    {"id": "terraform", "name": "Terraform State", "description": "Query and manage Terraform infrastructure state.", "mcp_server": "terraform", "full_definition": '{"type": "function"}'},
    {"id": "ansible", "name": "Ansible Playbooks", "description": "Execute and manage Ansible playbooks and inventory.", "mcp_server": "ansible", "full_definition": '{"type": "function"}'},
    
    # Communication & Collaboration Tools
    {"id": "slack_messages", "name": "Slack Message Retriever", "description": "Query Slack messages from connected workspaces. Can search by keyword or user.", "mcp_server": "slack", "full_definition": '{"type": "function"}'},
    {"id": "slack_users", "name": "Slack User Directory", "description": "Get information about Slack users and their profiles.", "mcp_server": "slack", "full_definition": '{"type": "function"}'},
    {"id": "slack_channels", "name": "Slack Channel Manager", "description": "List and manage Slack channels and permissions.", "mcp_server": "slack", "full_definition": '{"type": "function"}'},
    {"id": "teams_messages", "name": "Microsoft Teams Messages", "description": "Search and retrieve Microsoft Teams conversations.", "mcp_server": "teams", "full_definition": '{"type": "function"}'},
    {"id": "discord_messages", "name": "Discord Message Search", "description": "Search Discord server messages and user information.", "mcp_server": "discord", "full_definition": '{"type": "function"}'},
    {"id": "email_gmail", "name": "Gmail API", "description": "Read, search, and send emails using Gmail API.", "mcp_server": "gmail", "full_definition": '{"type": "function"}'},
    {"id": "email_outlook", "name": "Outlook Mail API", "description": "Access Outlook mailbox and manage emails.", "mcp_server": "outlook", "full_definition": '{"type": "function"}'},
    {"id": "telegram_bot", "name": "Telegram Bot API", "description": "Send and receive Telegram messages through bot interface.", "mcp_server": "telegram", "full_definition": '{"type": "function"}'},
    {"id": "twilio_sms", "name": "Twilio SMS", "description": "Send SMS messages and manage Twilio account.", "mcp_server": "twilio", "full_definition": '{"type": "function"}'},
    
    # Document & Content Tools
    {"id": "notion_pages", "name": "Notion Pages Retriever", "description": "Read and search Notion pages and databases.", "mcp_server": "notion", "full_definition": '{"type": "function"}'},
    {"id": "confluence_pages", "name": "Confluence Page Search", "description": "Search and retrieve Confluence documentation pages.", "mcp_server": "confluence", "full_definition": '{"type": "function"}'},
    {"id": "google_docs", "name": "Google Docs Reader", "description": "Read and search Google Docs and retrieve content.", "mcp_server": "google-docs", "full_definition": '{"type": "function"}'},
    {"id": "google_sheets", "name": "Google Sheets API", "description": "Read, write, and query Google Sheets.", "mcp_server": "google-sheets", "full_definition": '{"type": "function"}'},
    {"id": "pdf_parser", "name": "PDF Document Parser", "description": "Extract text and metadata from PDF files.", "mcp_server": "pdf", "full_definition": '{"type": "function"}'},
    {"id": "markdown_parser", "name": "Markdown Parser", "description": "Parse and extract information from Markdown documents.", "mcp_server": "markdown", "full_definition": '{"type": "function"}'},
    {"id": "json_validator", "name": "JSON Validator", "description": "Validate and parse JSON data structures.", "mcp_server": "json", "full_definition": '{"type": "function"}'},
    {"id": "xml_parser", "name": "XML Parser", "description": "Parse and query XML documents using XPath.", "mcp_server": "xml", "full_definition": '{"type": "function"}'},
    
    # Project Management & Issue Tracking
    {"id": "jira_issues", "name": "Jira Issue Tracker", "description": "Search and manage Jira issues and sprints.", "mcp_server": "jira", "full_definition": '{"type": "function"}'},
    {"id": "linear_issues", "name": "Linear Issue Manager", "description": "Query Linear issues and project management data.", "mcp_server": "linear", "full_definition": '{"type": "function"}'},
    {"id": "asana_tasks", "name": "Asana Task Manager", "description": "Manage tasks and projects in Asana.", "mcp_server": "asana", "full_definition": '{"type": "function"}'},
    {"id": "trello_boards", "name": "Trello Board Manager", "description": "Manage Trello boards, lists, and cards.", "mcp_server": "trello", "full_definition": '{"type": "function"}'},
    {"id": "monday_com", "name": "Monday.com Workspace", "description": "Access Monday.com boards and manage work items.", "mcp_server": "monday", "full_definition": '{"type": "function"}'},
    
    # Analytics & Monitoring Tools
    {"id": "google_analytics", "name": "Google Analytics", "description": "Query GA4 and Universal Analytics data.", "mcp_server": "analytics", "full_definition": '{"type": "function"}'},
    {"id": "mixpanel", "name": "Mixpanel Analytics", "description": "Query Mixpanel events and user analytics.", "mcp_server": "mixpanel", "full_definition": '{"type": "function"}'},
    {"id": "datadog", "name": "Datadog Monitoring", "description": "Query Datadog metrics and logs.", "mcp_server": "datadog", "full_definition": '{"type": "function"}'},
    {"id": "prometheus", "name": "Prometheus Metrics", "description": "Query Prometheus time-series metrics.", "mcp_server": "prometheus", "full_definition": '{"type": "function"}'},
    {"id": "grafana", "name": "Grafana Dashboards", "description": "Query Grafana dashboards and visualization data.", "mcp_server": "grafana", "full_definition": '{"type": "function"}'},
    {"id": "newrelic", "name": "New Relic APM", "description": "Query application performance monitoring data from New Relic.", "mcp_server": "newrelic", "full_definition": '{"type": "function"}'},
    {"id": "splunk", "name": "Splunk Search", "description": "Perform searches and retrieve logs from Splunk.", "mcp_server": "splunk", "full_definition": '{"type": "function"}'},
    {"id": "elastic_stack", "name": "Elastic Stack Logs", "description": "Query logs from Elasticsearch and Kibana.", "mcp_server": "elastic", "full_definition": '{"type": "function"}'},
    
    # Finance & Business Tools
    {"id": "stripe_api", "name": "Stripe Payments", "description": "Query Stripe transactions, customers, and subscription data.", "mcp_server": "stripe", "full_definition": '{"type": "function"}'},
    {"id": "shopify_store", "name": "Shopify Store Manager", "description": "Manage Shopify products, orders, and customers.", "mcp_server": "shopify", "full_definition": '{"type": "function"}'},
    {"id": "quickbooks", "name": "QuickBooks Accounting", "description": "Access QuickBooks financial data and transactions.", "mcp_server": "quickbooks", "full_definition": '{"type": "function"}'},
    {"id": "salesforce", "name": "Salesforce CRM", "description": "Query Salesforce records, accounts, and opportunities.", "mcp_server": "salesforce", "full_definition": '{"type": "function"}'},
    {"id": "hubspot_crm", "name": "HubSpot CRM", "description": "Access HubSpot contacts, deals, and sales pipeline.", "mcp_server": "hubspot", "full_definition": '{"type": "function"}'},
    {"id": "pipedrive", "name": "Pipedrive Sales", "description": "Manage Pipedrive deals and sales activities.", "mcp_server": "pipedrive", "full_definition": '{"type": "function"}'},
    {"id": "zendesk_support", "name": "Zendesk Support Tickets", "description": "Search and manage Zendesk support tickets and customer data.", "mcp_server": "zendesk", "full_definition": '{"type": "function"}'},
    {"id": "intercom", "name": "Intercom Customer Data", "description": "Access Intercom customer conversations and data.", "mcp_server": "intercom", "full_definition": '{"type": "function"}'},
    
    # AI & ML Tools
    {"id": "openai_api", "name": "OpenAI API", "description": "Call OpenAI models for text generation and embeddings.", "mcp_server": "openai", "full_definition": '{"type": "function"}'},
    {"id": "anthropic_claude", "name": "Anthropic Claude", "description": "Call Claude models for various AI tasks.", "mcp_server": "anthropic", "full_definition": '{"type": "function"}'},
    {"id": "huggingface_models", "name": "Hugging Face Models", "description": "Access and run models from Hugging Face hub.", "mcp_server": "huggingface", "full_definition": '{"type": "function"}'},
    {"id": "cohere_api", "name": "Cohere Language AI", "description": "Use Cohere API for NLP tasks and embeddings.", "mcp_server": "cohere", "full_definition": '{"type": "function"}'},
    {"id": "replicate_models", "name": "Replicate AI Models", "description": "Run machine learning models from Replicate.", "mcp_server": "replicate", "full_definition": '{"type": "function"}'},
    
    # Weather & Location Tools
    {"id": "weather_api", "name": "Weather API", "description": "Get current weather and forecasts by location.", "mcp_server": "weather", "full_definition": '{"type": "function"}'},
    {"id": "geolocation", "name": "Geolocation Lookup", "description": "Get geographic information for IP addresses or coordinates.", "mcp_server": "geolocation", "full_definition": '{"type": "function"}'},
    {"id": "maps_google", "name": "Google Maps", "description": "Search locations, get directions, and retrieve map data.", "mcp_server": "google-maps", "full_definition": '{"type": "function"}'},
    {"id": "openstreetmap", "name": "OpenStreetMap", "description": "Query OpenStreetMap data for locations and coordinates.", "mcp_server": "osm", "full_definition": '{"type": "function"}'},
    
    # Calendar & Time Tools
    {"id": "google_calendar", "name": "Google Calendar", "description": "Read, create, and manage Google Calendar events.", "mcp_server": "google-calendar", "full_definition": '{"type": "function"}'},
    {"id": "outlook_calendar", "name": "Outlook Calendar", "description": "Manage Outlook calendar events and availability.", "mcp_server": "outlook", "full_definition": '{"type": "function"}'},
    {"id": "calendly", "name": "Calendly Scheduling", "description": "Check Calendly availability and scheduling information.", "mcp_server": "calendly", "full_definition": '{"type": "function"}'},
    
    # Media & Video Tools
    {"id": "youtube_api", "name": "YouTube Video Search", "description": "Search YouTube videos and retrieve metadata.", "mcp_server": "youtube", "full_definition": '{"type": "function"}'},
    {"id": "vimeo_api", "name": "Vimeo Video Library", "description": "Manage Vimeo videos and retrieve video metadata.", "mcp_server": "vimeo", "full_definition": '{"type": "function"}'},
    {"id": "aws_mediaconvert", "name": "AWS Media Convert", "description": "Convert and process media files using AWS.", "mcp_server": "aws", "full_definition": '{"type": "function"}'},
    {"id": "ffmpeg", "name": "FFmpeg Media Tool", "description": "Process and convert audio/video files with FFmpeg.", "mcp_server": "ffmpeg", "full_definition": '{"type": "function"}'},
    
    # Social Media Tools
    {"id": "twitter_api", "name": "Twitter/X API", "description": "Search tweets and retrieve Twitter account data.", "mcp_server": "twitter", "full_definition": '{"type": "function"}'},
    {"id": "instagram_api", "name": "Instagram Graph API", "description": "Access Instagram business account data and insights.", "mcp_server": "instagram", "full_definition": '{"type": "function"}'},
    {"id": "facebook_api", "name": "Facebook Graph API", "description": "Query Facebook pages and retrieve social data.", "mcp_server": "facebook", "full_definition": '{"type": "function"}'},
    {"id": "linkedin_api", "name": "LinkedIn API", "description": "Access LinkedIn profile and company information.", "mcp_server": "linkedin", "full_definition": '{"type": "function"}'},
    {"id": "tiktok_api", "name": "TikTok API", "description": "Access TikTok video data and analytics.", "mcp_server": "tiktok", "full_definition": '{"type": "function"}'},
    
    # E-commerce & Marketplace Tools
    {"id": "amazon_product", "name": "Amazon Product Search", "description": "Search Amazon products and retrieve pricing/availability.", "mcp_server": "amazon", "full_definition": '{"type": "function"}'},
    {"id": "ebay_search", "name": "eBay Marketplace Search", "description": "Search eBay listings and retrieve auction data.", "mcp_server": "ebay", "full_definition": '{"type": "function"}'},
    {"id": "etsy_api", "name": "Etsy Shop Manager", "description": "Manage Etsy shop products and orders.", "mcp_server": "etsy", "full_definition": '{"type": "function"}'},
    {"id": "woocommerce", "name": "WooCommerce Store", "description": "Manage WooCommerce products, orders, and customers.", "mcp_server": "woocommerce", "full_definition": '{"type": "function"}'},
    
    # Email Marketing Tools
    {"id": "mailchimp", "name": "Mailchimp Email", "description": "Manage Mailchimp campaigns, lists, and subscribers.", "mcp_server": "mailchimp", "full_definition": '{"type": "function"}'},
    {"id": "sendgrid", "name": "SendGrid Email API", "description": "Send transactional emails via SendGrid.", "mcp_server": "sendgrid", "full_definition": '{"type": "function"}'},
    {"id": "active_campaign", "name": "ActiveCampaign CRM", "description": "Access ActiveCampaign contacts and automation data.", "mcp_server": "activecampaign", "full_definition": '{"type": "function"}'},
    
    # HR & Employee Tools
    {"id": "workday", "name": "Workday HCM", "description": "Access Workday employee and HR data.", "mcp_server": "workday", "full_definition": '{"type": "function"}'},
    {"id": "bamboohr", "name": "BambooHR Employee Data", "description": "Query BambooHR employee records and time off.", "mcp_server": "bamboohr", "full_definition": '{"type": "function"}'},
    {"id": "guidepoint", "name": "GuidePay Payroll", "description": "Access payroll and compensation data.", "mcp_server": "payroll", "full_definition": '{"type": "function"}'},
    
    # Legal & Compliance Tools
    {"id": "docusign", "name": "DocuSign eSignature", "description": "Send documents for signature via DocuSign.", "mcp_server": "docusign", "full_definition": '{"type": "function"}'},
    {"id": "contract_analyzer", "name": "Contract Analysis Tool", "description": "Analyze legal contracts for key terms and clauses.", "mcp_server": "legal", "full_definition": '{"type": "function"}'},
    
    # Utilities & Misc Tools
    {"id": "text_translator", "name": "Text Translator", "description": "Translate text between languages using translation APIs.", "mcp_server": "translator", "full_definition": '{"type": "function"}'},
    {"id": "ocr_document", "name": "OCR Document Scanner", "description": "Extract text from images and scanned documents.", "mcp_server": "ocr", "full_definition": '{"type": "function"}'},
    {"id": "qr_generator", "name": "QR Code Generator", "description": "Generate QR codes from text or URLs.", "mcp_server": "qr", "full_definition": '{"type": "function"}'},
    {"id": "barcode_scanner", "name": "Barcode Scanner", "description": "Decode and generate barcodes in various formats.", "mcp_server": "barcode", "full_definition": '{"type": "function"}'},
    {"id": "file_converter", "name": "File Format Converter", "description": "Convert files between different formats (images, docs, etc).", "mcp_server": "converter", "full_definition": '{"type": "function"}'},
    {"id": "password_manager", "name": "Password Manager API", "description": "Securely store and retrieve passwords.", "mcp_server": "vault", "full_definition": '{"type": "function"}'},
    {"id": "vpn_proxy", "name": "VPN Proxy Manager", "description": "Manage VPN connections and proxy settings.", "mcp_server": "network", "full_definition": '{"type": "function"}'},
    {"id": "crypto_wallet", "name": "Cryptocurrency Wallet", "description": "Query blockchain and cryptocurrency wallet data.", "mcp_server": "crypto", "full_definition": '{"type": "function"}'},
    {"id": "nft_marketplace", "name": "NFT Marketplace API", "description": "Search NFT collections and retrieve asset data.", "mcp_server": "nft", "full_definition": '{"type": "function"}'},
    {"id": "stock_market", "name": "Stock Market Data", "description": "Get stock prices, historical data, and market information.", "mcp_server": "stocks", "full_definition": '{"type": "function"}'},
    {"id": "forex_rates", "name": "Foreign Exchange Rates", "description": "Retrieve current and historical currency exchange rates.", "mcp_server": "forex", "full_definition": '{"type": "function"}'},
]