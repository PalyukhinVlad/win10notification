import win10toast

def Main():
    toast = win10toast.ToastNotifier()
    toast.show_toast(title="Hello, World!!!", msg="Im here", duration=10)

if __name__ == "__main__":
    Main()
