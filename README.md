<p align="center" style="color: #444">
  <h1 align="center">🔠 Telegram Translator</h1>
</p>
<p align="center" style="font-size: 1.2rem;">Automatically translate all outcoming messages.</p>

> **Warning**
> Abusing the API capabilities may lead to your Telegram account being blocked

## Configuration

This project uses a .env file for configuration with the following structure:

```bash
API_ID=<API_ID> # from my.telegram.org/apps
API_HASH="<API_HASH>" # from my.telegram.org/apps
FIRST_LANGUAGE="es" # language code or language name from readthedocs.org/projects/py-googletrans/downloads/pdf/latest/
SECOND_LANGUAGE="en" # language code or language name from readthedocs.org/projects/py-googletrans/downloads/pdf/latest
```

To get the `API_ID` and `API_HASH` for your Telegram application, follow these steps:

1. Go to the [Telegram API Portal](https://my.telegram.org/auth).
2. Login with your phone number.
3. Click on the API development tools link.
4. Click on the Create New Application button.
5. Fill in the required fields and click on the Create button.
6. Your `API_ID` and `API_HASH` will be displayed on the next page.

## Usage

To use this project, clone the repository and install the required dependencies:

1.  [Install python](https://www.python.org/downloads/)
2.  Copy code below in the terminal:

```bash
git clone https://git@github.com:qpwedev/telegram-translator.git
cd telegram-translator
```

3. Create a `.env` file in the root directory of the project and fill it with your API_ID, API_HASH, and your chosen FIRST_LANGUAGE and SECOND_LANGUAGE.
4. Install the required dependencies:

```
pip3 install -r requirements.txt
```

Finally, run the script:

```bash
python3 ./src/run.py
```
