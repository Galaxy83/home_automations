""" This file contains all the routines that are run by cron. """
from qbittorrent import Client

from methods import get_last_state, set_last_state, get_current_state

qb = Client('http://192.168.50.100:8080/')


def pause_all_torrents_if_online(key, name):
    """ Pauses all torrents when the PS5 is online and resumes them when the PS5 is offline. """

    is_online = get_current_state(key, name) == 'online'
    if is_online and get_last_state(name) == 'offline':
        qb.pause_all()
        print('Pausing all torrents.')
        set_last_state(name, 'online')
        return

    if not is_online and get_last_state(name) == 'online':
        for torrent in qb.torrents():
            if torrent['amount_left'] > 0:
                qb.resume(torrent['hash'])
        print('Resuming all torrents.')
        set_last_state(name, 'offline')
        return

    print('Doing nothing.')
