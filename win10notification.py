import win10toast

def Main():
    toast = win10toast.ToastNotifier()
    toast.show_toast(title="Hello, World!!!", msg="Some Random Text", duration=5)

if __name__ == "__main__":
    Main()
