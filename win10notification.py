import win10toast


def main():
    toast = win10toast.ToastNotifier()
    toast.show_toast(title="Hello, World!!!", msg="Im here", duration=10)


if __name__ == "__main__":
    main()
