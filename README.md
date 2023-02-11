# Timeburglar. A kittypaws plugin

A plugin to break time synchronization on a host with the use of [kittypaws](https://github.com/subatiq/kittypaws).

## Installation

Put the `main.py` into `~/.kittypaws/plugins/timeburglar` folder.

## Example config

```yaml
plugins:
# Disrupting host time
- timeburglar:
    shift: 1
    startup: hot
    frequency: fixed
    interval: PT60S
```

`shift` - amount of seconds to shift time on the host for

The rest is described in [kittypaws](https://github.com/subatiq/kittypaws) README.
