# kouetsupy | 幸悦py

This is a simple command-line news application written in Python. It fetches the latest news headlines using the NewsAPI and displays them in the terminal. 

**Project Structure**

- `config.yaml` - Configuration file containing API key, default country code, and API URL.
- `main.py` - Entry point for the application. It loads configuration, fetches news, and displays it.
- `news/`
  - `fetcher.py` - Module for fetching news from the API.
  - `display.py` - Module for displaying news headlines in the terminal.
- `utils/`
  - `config_loader.py` - Module for loading the YAML configuration file.
- `requirements.txt` - File listing the Python dependencies.

**Setup**

1. **Configure API Key**

   Obtain an API key from [NewsAPI](https://newsapi.org/) and add it to the `config.yaml` file. Update the `api_key` field with your API key.
   
2. **Install Dependencies**

   Then, install the required Python packages. Navigate to the project directory and run:
   ```
   pip install -r requirements.txt
   ```
   
**Create an Alias**

For easier access to the application, you can create a command alias in your shell configuration file.

- **For Bash/Zsh Users**

  Add the following line to your `.bashrc` or `.zshrc` file:
  ```
  alias news='python /path/to/your/news_terminal_app/main.py'
  ```

  After adding the alias, reload your shell configuration:
  ```
  source ~/.bashrc
  ```
  or
  ```
  source ~/.zshrc
  ```

**Notes**

- Ensure that the `config.yaml` file is correctly configured before running the application.
- The API key is required for fetching news; otherwise, the application will not work.

**License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the paths and details according to your specific setup.
