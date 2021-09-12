def make_album(composer, album_name, n_tracks=None):
    """Строит словарь с описанием музыкального альбома"""
    gloss = {
        "composer": composer,
        "album": album_name,
        }    
    if type(n_tracks) == type(int()):
        gloss["n_tracks"] = n_tracks
        
    return gloss

print("Collection of info...\n")
while True:
    comp = input("Composer: ")
    album = input("Album title: ")
    n_tracks = int(input("Number of tracks: "))

    print("\nGlossary added:")
    print("\t", make_album(comp, album, n_tracks))
    
    extension = input("\nTo continue? (yes/no) ")
    if extension.lower() == "no":
        break
    print()    
