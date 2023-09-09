# Bitbucket Repository Cloner

## Purpose
This script automates the process of cloning all repositories from a Bitbucket account. It fetches the list of repositories using Bitbucket's REST API and clones each one into a designated folder.

## Dependencies
- Python 3.x
- `requests` library

Install the dependencies using pip:

```bash
pip install requests
```

## Usage
Run the script using Python:

```bash
python script_name.py [destination_folder]
```

## Arguments
`destination_folder` (optional): The folder where the cloned repositories will be stored. Default is `bitbucket_repo`.

## Limitations
- The script currently does not support authenticated requests. As such, it can only clone public repositories.
- Error handling is minimal, so the script may not gracefully handle all edge cases.

## License
MIT
