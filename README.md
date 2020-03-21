# Odin

_A silly service status checker in Python_

## What Is This?

This is a simple Python application intended to provide insights about the reachability of different targets.
The main goal of this app is to monitor multiple URLs and export metrics using Python's [prometheus\_client](https://github.com/prometheus/client_python).

## How To Use This

### Local

1. Clone this repository `git clone https://github.com/tbobm/odin`
2. Install the requirements `pip install -r requirements.txt`
3. (optional) Edit the configuration file
4. Install odin `python setup.py install`
5. Make sure the `ODIN_CONFIG_FILE` variable points to the configuration file you want

### Docker

1. Run the container `docker run -it -p 8000:8000 --rm massardtheo/odin`
2. (optional) Edit the configuration beforehand and add `-v MYCONFIG:/app/odin.yaml`

## Testing

Well, I'm guilty right now. No testing yet. See [Testing](https://github.com/tbobm/odin/issues/12).

## Bugs and suggestions

Feel free to create an issue as exhaustive as possible regarding the bugs or ideas you might have.

## Development

Every contribution is welcome, I encourage you to create a Pull Request if you want to integrate your work.

## Documentation

Well, nothing is available right now.
