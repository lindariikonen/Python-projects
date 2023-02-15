"""
COMP.CS.100 Project 3: Travel route optimizer
Made by: Linda Riikonen
"""


def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: ?????, A data structure of an unspecified type (you decide)
           which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stored twice.
    """

    # +--------------------------------------+
    # |                                      |
    # |     DO NOT MODIFY THIS FUNCTION!     |
    # |                                      |
    # +--------------------------------------+

    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city,
                                                                 neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours,
                                             key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: dict, a data structure containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """

    if city in data:
        return list(data[city])

    else:
        return []


def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: dict, a data structure containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """

    distance = 0

    # If the destination is unknown, return None
    if destination not in data[departure]:
        return None

    # Add the destination between departure and destination cities
    else:
        distance += int(data[departure][destination])

    return distance


def route_length(route, distance_data):
    """
    Calculate the route's length and print it.

    :param route: Travel route from previously given departure city to
           destination city
    :param distance_data: dict, a data structure containing the distance
           information between the known cities.
    """

    # Print cities' names with a dash between them
    for cities in range(0, len(route)):
        print(f"{cities}", end="")

        if cities != (len(route) - 1):
            print("-", end="")

        # Print the route's length after the cities' names
        else:
            dist = 0

            for index in range(0, len(route) - 1):
                departure = str([index])
                destination = str([index + 1])
                dist += int(distance_data[departure][destination])
            print(f" {dist}")


def remove_road(distance_data):
    """
    Remove road between two known cities. Print error message if either city
    is unknown.

    :param distance_data: dict, a data structure containing the distance
           information between the known cities.
    """

    departure = input("Enter departure city: ")

    # Print error message if departure city is not known
    if departure not in distance_data:
        print(f"Error: \'{departure}\' is unknown.")

    else:
        destination = input("Enter destination city: ")

        # Print error message if destination city is not known
        if destination not in distance_data[departure]:
            print(f"Error: missing road segment between \'{departure}"
                  f"\' and \'{destination}\'.")

        # Remove given road segment if both cities are known
        else:
            del distance_data[departure][destination]


def add_road(distance_data):
    """
    Add a road segment between two cities. Print an error message if
    the given distance between cities is not an integer.

    :param distance_data: dict, a data structure containing the distance
           information between the known cities.
    """

    departure = input("Enter departure city: ")
    destination = input("Enter destination city: ")
    distance = input("Distance: ")

    # Try to change the inputted distance's type into an integer. If the change
    # is successful, create given road segment
    try:
        int(distance)
        if departure not in distance_data:
            path = {destination: distance}
            distance_data[departure] = path
        else:
            distance_data[departure][destination] = distance
            # Create a road segment from the destination city to itself if the
            # city was unknown
            if destination not in distance_data:
                path = {destination: 0}
                distance_data[destination] = path

    # If distance's type can't be changed, print error message
    except ValueError:
        print(f"Error: \'{distance}\' is not an integer.")


def print_all(distance_data):
    """
    Print all departure cities and adjacent cities in alphabetical order.

    :param distance_data: dict, a data structure containing the distance
           information between the known cities.
    """

    for departure in sorted(distance_data):
        for destination in sorted(distance_data[departure]):
            if departure == destination:
                continue
            else:
                print(f"{departure:<13} {destination:<13} "
                      f"{distance_data[departure][destination]:>5}")


def read_distance_file(file_name):
    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: dict | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
    """

    # Try to open the given file in read mode and store the file's data into
    # a nested dictionary
    try:
        file = open(file_name, mode="r", encoding="utf-8")
        route = {}

        for line in file:
            departure, destination, distance = line.rstrip().split(";")

            if departure not in route:
                route[departure] = {}
            route[departure][destination] = int(distance)

    # If the given file can't be opened, return None
    except OSError:
        return None

    # Close the file and return the created dictionary
    file.close()
    return route


def calculate_route(data):
    """
    Asks the user for two cities and check that they are known. Display the
    route calculated by the find_route function along with its total length.

    :param data: dict, a data structure containing the distance
           information between known cities.
    """

    departure = input("Enter departure city: ")

    # Check that departure city is known
    if departure in data:
        destination = input("Enter destination city: ")
        route = find_route(data, departure, destination)

        # Check that destination city is known, and it's possible to get there
        if destination not in route or route == []:
            print(f"No route found between '{departure}' and '{destination}'.")

        # Calculate the route's length and store it in total_distance
        else:
            total_distance = 0

            for city in range(0, (len(route) - 1)):
                distance = distance_to_neighbour(data, route[city],
                                                 route[city + 1])
                if distance is None:
                    distance = 0

                total_distance += distance
                print(route[city], "-", sep="", end="")

            print(route[-1], " (", total_distance, " km)", sep="")

    # Check if the departure city is saved as a destination
    else:
        _data = data
        try:
            _data = _data[departure]
        except KeyError:
            print(f"Error: \'{departure}\' is unknown.")
            return

        destination = input("Enter destination city: ")
        print(f"No route found between '{departure}' and '{destination}'.")


def main():
    # input_file = input("Enter input file name: ")
    input_file = "distances1.txt"

    # Store the data into a dictionary
    distance_data = read_distance_file(input_file)

    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")
        # Available inputs:
        # display = display all known connections between cities
        # add = add a road segment between two cities
        # remove = remove road segment between two previously known cities
        # neighbours = display all known connections to a certain city
        # route = calculate route and distance between two known cities

        if action == "":
            print("Done and done!")
            return

        elif "display".startswith(action):
            print_all(distance_data)

        elif "add".startswith(action):
            add_road(distance_data)

        elif "remove".startswith(action):
            remove_road(distance_data)

        elif "neighbours".startswith(action):
            departure = input("Enter departure city: ")

            if departure in distance_data:
                for destination in sorted(distance_data[departure]):
                    if departure == destination:
                        continue
                    else:
                        print(f"{departure:<13} {destination:<13} "
                              f"{distance_data[departure][destination]:>5}")
            else:
                print(f"Error: \'{departure}\' is unknown.")

        elif "route".startswith(action):
            calculate_route(distance_data)

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
