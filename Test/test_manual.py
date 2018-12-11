import starwars_api.StarSearch

searcher = starwars_api.StarSearch.StarSearch()

built_dict = searcher.complete_object_dict_maker()
print("Built Dict: " + str(built_dict))