# executed directly by py, __name__ = __main__
# import as a module, __name__ = dunder


print('We start off in:', __name__)
if __name__ == "__main__":
    print("And end up in:", __name__)
