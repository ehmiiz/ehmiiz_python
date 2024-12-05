# function that generates music data
# number_of_songs is optional
def make_album(artist_name, album_name, number_of_songs = None):
    # Create an empty dict
    return_value = {}
    
    return_value['artist_name'] = artist_name
    return_value['album_name'] = album_name
    
    if number_of_songs:
        return_value['number_of_songs'] = number_of_songs
    
    return return_value

# Generate dictionaries using the function
music_data = make_album('Soilwork', 'Verkligheten')
music_data_new = make_album('Soilwork', 'Övergivenheten', 15)


# Print data
print(music_data)
print(music_data_new)

# Make a while-loop that fills in user data
while(True):
    print('Type "q" to quit at any time.')
    art_name = input("Name of artist: ")
    if art_name == 'q':
        break
    
    alb_name = input("Name of album: ")
    if alb_name == 'q':
        break
    
    music_data = make_album(art_name, alb_name)
    
    print(music_data)