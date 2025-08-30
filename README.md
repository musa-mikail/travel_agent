# Travel Agent AI

A Streamlit web application that helps users plan holidays using an AI agent. The app generates city recommendations based on user interests, budget, and travel dates.

## Features

- **AI-powered destination planning**: Suggests top cities matching your preferences.
- **Streamlit interface**: Simple and interactive user experience.
- **Environment-based configuration**: Secure API keys and settings via `.env`.

## Getting Started

### Prerequisites

- Python 3.12+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/travel-agent.git
    cd travel-agent
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory (see example below).

### .env Example

```
DATABASE_URL=your_database_url
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
APP_URL=
APP_TITLE=
```

### Running the App

```sh
streamlit run app/main.py
```

## Usage

1. Enter your interests, budget, and travel dates.
2. Click "Lets begin" to get AI-powered city recommendations.

## Project Structure

```
.env
.gitignore
requirements.txt
app/
    __init__.py
    agents.py
    main.py
```

- [`app/agents.py`](app/agents.py): AI agent logic for destination planning.
- [`app/main.py`](app/main.py): Streamlit UI and user interaction.

## License

MIT

## Author

Musa Mikail