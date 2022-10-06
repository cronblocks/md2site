# *****************************************************************************************
# * Purpose:
# *     Main application - loading and orchestrating other application components
# *
# *
# *****************************************************************************************
# * Author: Usama
# *
# *****************************************************************************************
# * Changes:
# *
# * Date         Changed by      Description
# * ----         ----------      -----------
# *
# *
# *
# *
# *****************************************************************************************

from providers.settings import Settings


def main():
    print("Hi from md2site")
    print("")
    
    settings: Settings = Settings()

    settings.print()


if __name__ == "__main__":
    main()
