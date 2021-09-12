def make_album(composer, album_name, n_tracks=None):
    """Строит словарь с описанием музыкального альбома"""
    gloss = {
        "composer": composer,
        "album": album_name,
        }    
    if type(n_tracks) == type(int()):
        gloss["n_tracks"] = n_tracks
        
    return gloss

print(make_album(composer="gorillaz", album_name="19-2000"))
print(make_album(composer="otis mcdonald", album_name="ever felt pt.1"))
print(make_album(composer="the jacksons", album_name="blame it on the boogie"))
print(make_album(composer="потап и настя", album_name="выкрутасы",
                 n_tracks = 64))
