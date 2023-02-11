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

`target` - container in which disconnection should be simulated\
`ip` - which address to disconnect\
`unavailable_seconds` - amount of time the `ip` will be unavailable for the `target`
