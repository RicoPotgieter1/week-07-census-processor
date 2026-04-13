import csv
from datetime import datetime

quit = False

while quit == False:
    options = ["view all", "filter by language", "stats", "write report", "exit"]
    for i in range(len(options)):
        print(f"{i + 1}. {options[i].title()}")

    choice = input("Enter your choice (1-5): ").strip().lower()
    print()

    if choice == "2" or choice == "filter by language":

        language = input("Choose a language to filter by: ").strip().title()

        with open("Read_and_Write\\sa_census.csv") as f:
            data = list(csv.DictReader(f))
            filtered_provinces = [p for p in data if language in p["main_language"]]
            if not filtered_provinces:
                print("This language is not one of the main languages spoken in South-Afrika or please check your spelling and try again.")
            print()
            for i in range(len(filtered_provinces)):
                for key, value in filtered_provinces[i].items():
                    print(f"{key:<20}: {value}")
                print()
                    
    elif choice == "3" or choice == "stats":
        total_pop = 0
        total_area = 0
        density_ranking = []
        with open("Read_and_Write\\sa_census.csv") as f:
            data = list(csv.DictReader(f))
            for i in range(len(data)):
                total_pop += int(data[i]["population"])
                total_area += int(data[i]["area_km2"])
                gdp_per_province = int(data[i]["gdp_per_capita"]) * int(data[i]["population"])
                density = int(data[i]["population"]) / int(data[i]["area_km2"])
                density_ranking.append((data[i]["name"], density, gdp_per_province))

            average_area = total_area / len(data)
            most_pop_province = [p for p in data if int(p["population"]) == max(int(p["population"]) for p in data)]
            least_pop_province = [p for p in data if int(p["population"]) == min(int(p["population"]) for p in data)]

            density_ranking.sort(key=lambda d: d[1], reverse= True)
            print("---------- Density and GDP per Province Ranking ----------\n")

            title1, title2, title3 = "Province", "Density (people/km2)", "GDP per Province"

            print(f"{title1} {title2:>32} {title3:>24}\n")
            for i in range(len(density_ranking)):
                print(f"{density_ranking[i][0] :<20} {density_ranking[i][1]:>10,.2f} {density_ranking[i][2]:>35,.2f}\n")
            print("-" * 60)

            print(f"{"Most populated province":<25}: {most_pop_province[0]['name']}")
            print(f"{"Least populated province":<25}: {least_pop_province[0]['name']}")
            print(f"{"Average area":<25}: {average_area:,.2f}km2")
            print(f"{"Total population":<25}: {total_pop:,}")
            print()
            
    elif choice == "1" or choice == "view all":
        total_pop = 0
        with open("Read_and_Write\\sa_census.csv") as f:
            data = list(csv.DictReader(f))
            for p in data:
                total_pop += int(p["population"])
                p["density"] = round(int(p["population"]) / int(p["area_km2"]), 2)
                p["gdp_per_province"] = f"{int(p["gdp_per_capita"]) * int(p["population"]):,}"
            
                for key, value in p.items():
                    print(f"{key:<20}: {value}")
                print()

            largest_province_pop = [p for p in data if int(p["population"]) == max(int(p["population"]) for p in data)]
            smallest_province = [p for p in data if int(p["area_km2"]) == min(int(p["area_km2"]) for p in data)]

            
            print(f"Province with the largest population: {largest_province_pop[0]['name']}")
            print(f"Smallest Province (km2): {smallest_province[0]['name']}")
            print(f"Total Population of all provinces: {total_pop:,}")
            print()

    elif choice == "4" or choice == "write report":
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

        with open("census_report.txt", "w") as w:
            w.write("Census report of South-Africa's statistics\n")
            w.write("-"*50)
            w.write("\n")

            total_pop = 0
            total_area = 0
            density_ranking = []
            with open("Read_and_Write\\sa_census.csv") as f:
                data = list(csv.DictReader(f))
                for i in range(len(data)):
                    total_pop += int(data[i]["population"])
                    total_area += int(data[i]["area_km2"])
                    gdp_per_province = int(data[i]["gdp_per_capita"]) * int(data[i]["population"])
                    density = int(data[i]["population"]) / int(data[i]["area_km2"])
                    density_ranking.append((data[i]["name"], density, gdp_per_province))
                    
                    
                average_area = total_area / len(data)
                most_pop_province = [p for p in data if int(p["population"]) == max(int(p["population"]) for p in data)]
                least_pop_province = [p for p in data if int(p["population"]) == min(int(p["population"]) for p in data)]

                w.write(f"{"Most populated province":<25}: {most_pop_province[0]['name']}\n")
                w.write(f"{"Least populated province":<25}: {least_pop_province[0]['name']}\n")
                w.write(f"{"Average area(km2)":<25}: {average_area:,.2f}\n")
                w.write(f"{"Total population":<25}: {total_pop:,}\n\n")

                density_ranking.sort(key=lambda d: d[1], reverse= True)
                w.write("---------- Density and GDP per Province Ranking ----------\n")

                title1, title2, title3 = "Province", "Density (people/km2)", "GDP per Province"

                w.write(f"{title1} {title2:>32} {title3:>24}\n")
                for i in range(len(density_ranking)):
                    w.write(f"{density_ranking[i][0] :<20} {density_ranking[i][1]:>10,.2f} {density_ranking[i][2]:>35,.2f}\n")
                w.write("-" * 60)

            w.write("\n\n")
            w.write("-"*60)
            w.write(f"\nTimestamp: {formatted_now}")

    elif choice == "5" or choice == "exit":
        quit = True

    else:
        print("Please enter a number between 1 - 5.")
        print()