import subprocess
import datetime
import requests
import os
import webbrowser

def get_weather(city):
    # Make a request to the Weather API to get information
    api_key = "Y09c418b7c9538c528ccc9bb7205542a4"  # Insert your OpenWeatherMap API key here
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Weather in {city.title()}: {temp}°C, {desc}")
    else:
        print("Weather information couldn't be retrieved.")

def set_alarm():
    # Alarm setting function
    alarm_time = input("Enter the alarm time (HH:MM): ")
    # Set the alarm here (using a timer or notification function)

def file_operations():
    # Code for file/directory operations can be added here
    path = input("Enter the directory path to show: ")
    if os.path.exists(path):
        files = os.listdir(path)
        print("Files:")
        for file in files:
            print(file)
    else:
        print("Directory not found.")

def search_info(topic):
    # Function to search information about a specific topic
    wikipedia_api = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=&titles={topic}"
    response = requests.get(wikipedia_api)
    if response.status_code == 200:
        data = response.json()
        page_id = list(data['query']['pages'].keys())[0]
        info = data['query']['pages'][page_id]['extract']
        print(f"Information about {topic}:\n{info}")
    else:
        print("Information not found.")

def play_music():
    try:
        subprocess.run(['spotify'], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Spotify program not found. Please make sure it's installed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def run_scrcpy():
    try:
        subprocess.run(['scrcpy'])
    except FileNotFoundError:
        print("scrcpy not found. Please make sure it's installed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("Hello! My name is Muhtar. How can I assist you?")
    print("Type 'phone' to check your phone.")

    while True:
        command = input("Enter your command (Type 'exit' to quit): ")

        if command.lower() == 'exit':
            print("Muhtar is shutting down. Goodbye!")
            break
        elif command.lower() == 'phone':
            print("Opening your phone...")
            run_scrcpy()
        elif command.lower() == 'time':
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {current_time}")
        elif command.lower() == 'date':
            current_date = datetime.date.today().strftime("%d/%m/%Y")
            print(f"Current date: {current_date}")
        elif command.lower() == 'weather':
            city = input("Enter the city for weather information: ")
            get_weather(city)
        elif command.lower() == 'alarm':
            set_alarm()
        elif command.lower() == 'file':
            file_operations()
        elif command.lower() == 'search':
            topic = input("Enter the topic you want to search: ")
            search_info(topic)
        elif command.lower() == 'music':
            print("Opening your music...")
            play_music()
        elif command.lower() == 'take note':
            note = input("Enter your note: ")
            with open('notes.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()}: {note}\n")
            print("Your note has been saved.")
        else:
            print("Command not recognized. Please try again.")


def show_available_commands():
    # Kullanıcının mevcut komutları görmesini sağlayan işlev
    print("""
    Available Commands:
    - 'phone' : Check your phone.
    - 'time' : Show the current time.
    - 'date' : Show the current date.
    - 'weather' : Get weather information for a city.
    - 'alarm' : Set an alarm.
    - 'file' : Perform file/directory operations.
    - 'search' : Search information about a specific topic.
    - 'music' : Play music.
    - 'take note' : Take a note.
    - 'exit' : Shutdown Muhtar.
    """)

def main():
    print("Hello! My name is Muhtar. How can I assist you?")
    print("Type 'help' to see the list of available commands.")

    while True:
        command = input("Enter your command (Type 'exit' to quit): ")


        if command.lower() == 'exit':
            print("Muhtar is shutting down. Goodbye!")
            break
        elif command.lower() == 'phone':
            print("Opening your phone...")
            run_scrcpy()
        elif command.lower() == 'music':
            print("Opening Spotify for music...")
            play_music()
        # Diğer komutlar ve işlevler
        elif command.lower() == 'help':
            show_available_commands()
        else:
            print("Command not recognized. Please try again.")
if __name__ == "__main__":
    main()
