show_db_query = f"""SELECT Name, Title, Command
                    FROM Animals
                    INNER JOIN AnimalSpecies ON Kind = AnimalSpecies.id
                    INNER JOIN Commands ON Commands = Commands.id"""