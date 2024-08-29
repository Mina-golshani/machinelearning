import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    sorce_neighbors = neighbors_for_person(source)
    target_neighbors = neighbors_for_person(target)

    for person_2 in sorce_neighbors:
        if person_2[1] == '102':
            m1 = person_2[0]
            found_it = [(m1, '102')]
            break
        else:
            pass
    else:
        for person_2 in sorce_neighbors:
            n2 = neighbors_for_person(person_2[1])
            for person_3 in n2:
                if person_3[1] == '102':
                    found_it = [person_2, person_3]
                    break
                else:
                    pass
        else:
            for person_2 in sorce_neighbors:
                n2 = neighbors_for_person(person_2[1])
                for person_3 in n2:
                    n3 = neighbors_for_person(person_3)
                    for person_4 in n3:
                        if person_4[1] == '102':
                            found_it = [person_2, person_3, person_4]
                            break
                        else:
                            pass
            else:
                for person_2 in sorce_neighbors:
                    n2 = neighbors_for_person(person_2[1])
                    for person_3 in n2:
                        n3 = neighbors_for_person(person_3)
                        for person_4 in n3:
                            n4 = neighbors_for_person(person_4)
                            for person_5 in n4:
                                if person_5[1] == '102':
                                    found_it = [person_2, person_3, person_4, person_5]
                                    break
                                else:
                                    pass
                else:
                    for person_2 in sorce_neighbors:
                        n2 = neighbors_for_person(person_2[1])
                        for person_3 in n2:
                            n3 = neighbors_for_person(person_3)
                            for person_4 in n3:
                                n4 = neighbors_for_person(person_4)
                                for person_5 in n4:
                                    n5 = neighbors_for_person(person_5)
                                    for person_6 in n5:
                                        if person_6[1] == '102':
                                            found_it = [person_2, person_3, person_4, person_5, person_6]
                                            break
                                        else:
                                            pass
                    else:
                        for person_2 in sorce_neighbors:
                            n2 = neighbors_for_person(person_2[1])
                            for person_3 in n2:
                                n3 = neighbors_for_person(person_3)
                                for person_4 in n3:
                                    n4 = neighbors_for_person(person_4)
                                    for person_5 in n4:
                                        n5 = neighbors_for_person(person_5)
                                        for person_6 in n5:
                                            n6 = neighbors_for_person(person_6)
                                            for person_7 in n6:
                                                if person_7[1] == '102':
                                                    found_it = [person_2, person_3, person_4, person_5, person_6, person_7]
                                                    break
                                                else:
                                                    pass
                                            else:
                                                return None

    for person_2 in target_neighbors:
        if person_2[1] == '102':
            m1 = person_2[0]
            found_target = [(m1, target)]
            break
        else:
            pass
    else:
        for person_2 in target_neighbors:
            n2 = neighbors_for_person(person_2[1])
            for person_3 in n2:
                if person_3[1] == '102':
                    found_target = [(person_3[0], person_2[1]), (person_2[0], target)]
                    break
                else:
                    pass
        else:
            for person_2 in target_neighbors:
                n2 = neighbors_for_person(person_2[1])
                for person_3 in n2:
                    n3 = neighbors_for_person(person_3)
                    for person_4 in n3:
                        if person_4[1] == '102':
                            found_target = [(person_4[0], person_3[1]), (person_3[0], person_2[1]), (person_2[0], target)]
                            break
                        else:
                            pass
            else:
                for person_2 in target_neighbors:
                    n2 = neighbors_for_person(person_2[1])
                    for person_3 in n2:
                        n3 = neighbors_for_person(person_3)
                        for person_4 in n3:
                            n4 = neighbors_for_person(person_4)
                            for person_5 in n4:
                                if person_5[1] == '102':
                                    found_target = [(person_5[0], person_4[1]), (person_4[0], person_3[1]), (person_3[0], person_2[1]), (person_2[0], target)]
                                    break
                                else:
                                    pass
                else:
                    for person_2 in target_neighbors:
                        n2 = neighbors_for_person(person_2[1])
                        for person_3 in n2:
                            n3 = neighbors_for_person(person_3)
                            for person_4 in n3:
                                n4 = neighbors_for_person(person_4)
                                for person_5 in n4:
                                    n5 = neighbors_for_person(person_5)
                                    for person_6 in n5:
                                        if person_6[1] == '102':
                                            found_target = [(person_6[0], person_5[1]), (person_5[0], person_4[1]), (person_4[0], person_3[1]), (person_3[0], person_2[1]), (person_2[0], target)]
                                            break
                                        else:
                                            pass
                    else:
                        for person_2 in target_neighbors:
                            n2 = neighbors_for_person(person_2[1])
                            for person_3 in n2:
                                n3 = neighbors_for_person(person_3)
                                for person_4 in n3:
                                    n4 = neighbors_for_person(person_4)
                                    for person_5 in n4:
                                        n5 = neighbors_for_person(person_5)
                                        for person_6 in n5:
                                            n6 = neighbors_for_person(person_6)
                                            for person_7 in n6:
                                                if person_7[1] == '102':
                                                    found_target = [(person_6[0], person_5[1]), (person_5[0], person_4[1]), (person_4[0], person_3[1]), (person_3[0], person_2[1]), (person_2[0], target)]
                                                    break
                                                else:
                                                    pass
                                            else:
                                                return None

    return found_it + found_target
    



def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
