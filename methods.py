""" Methods for the asuswrt component"""

from asuswrt import AsusWRT

import my_logger

router = AsusWRT()


def get_last_state(name):
    """Get the last state of a client"""
    with open(f"states/{name}_state.txt", "r", encoding="utf-8") as file:
        state = 'offline'
        if file.read() == 'online':
            state = 'online'
        my_logger.init(name).info(f"Last state of {name}: {state}")
        return state


def set_last_state(name, state):
    """Set the last state of a client"""
    with open(f"states/{name}_state.txt", "w+", encoding="utf-8") as file:
        my_logger.init(name).info(f"Setting last state of {name} to {state}")
        file.write('online' if state == 'online' else 'offline')


def get_current_state(key, name):
    """Check if a client is online"""
    state = 'offline'
    clients = router.get_online_clients()
    for client in clients:
        if getattr(client, key) == name and client.isOnline == '1':
            state = 'online'
            break
    my_logger.init(name).info(f"Current state of {name}: {state}")
    return state
