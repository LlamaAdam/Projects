import json
from swgohhelp import SwgohHelp

def get_arena_rank(swgoh, ally_code):
    """
    Get the arena rank of a player with a given ally code.

    :param swgoh: SwgohHelp client instance
    :param ally_code: The ally code of the player
    :return: The arena rank of the player or None if not found
    """
    player_data = swgoh.fetch_players(ally_code)
    if player_data:
        player = player_data[0]
        arena_data = player.get('arena', {})
        char_arena_data = arena_data.get('char', {})
        return char_arena_data.get('rank')
    return None

def main():
    # Your SWGoH.help API credentials
    settings = {
        'username': 'YOUR_USERNAME',
        'password': 'YOUR_PASSWORD',
        'client_id': 'YOUR_CLIENT_ID',
        'client_secret': 'YOUR_CLIENT_SECRET'
    }
    
    # Instantiate the client
    swgoh = SwgohHelp(settings)

    # Your SWGoH ally code
    ally_code = 'YOUR_ALLY_CODE'
    
    # Get and print the arena rank
    arena_rank = get_arena_rank(swgoh, ally_code)
    if arena_rank is not None:
        print(f'Arena Rank: {arena_rank}')
    else:
        print('Could not retrieve arena rank.')

if __name__ == '__main__':
    main()
