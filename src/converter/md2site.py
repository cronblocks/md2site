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
from processing.processing_pipeline import Pipeline


def main():
    print("Hello from md2site")
    print("")
    
    settings: Settings = Settings()
    pipeline: Pipeline = Pipeline(settings)

    settings.print()
    pipeline.proceed()


if __name__ == "__main__":
    main()
