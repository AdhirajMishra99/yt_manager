
import json 

# file_name = 'utoob.txt'

def load_data():
    try:
        with open('utoob.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('utoob.txt', 'w') as file:
        json.dump(videos, file)


def list_all_vdeos(videos):
    print("\n")
    print("*" * 80)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 80)
    return "video listed sucsessfully...!"


def add_vdeo(videos):
    name = input("enter video name: ")
    time = input("enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("video added...!")


def update_vdeo(videos):
    list_all_vdeos(videos)
    index = int(input("enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("enter the new video name: ")
        time = input("enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("video updated successfully...!")
    else:
        print("invalid index chosen!")


def delete_vdeo(videos):
    list_all_vdeos(videos)
    index = int(input("enter the video number you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("video deleted sucessfully...!")
    else:
        print("invalid video index entered")


def main():
    videos = load_data()
    while True:
        print("\n youtube manager | choose option")
        print("1. list all youtube videos ")
        print("2. add youtube video ")
        print("3. update youtube video details ")
        print("4. delete youtube video ")
        print("5. exit")
        choice = input("enter the choice: ")
        # print(videos)
        match choice:
            case '1':
                list_all_vdeos(videos)
            case '2':
                add_vdeo(videos)
            case '3':
                update_vdeo(videos)
            case '4':
                delete_vdeo(videos)
            case '5':
                print("Good Bye....")
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()
