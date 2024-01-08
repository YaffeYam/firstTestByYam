from tools.numbers import simp, comp
from tools import col

class ModuleImporter:
    @staticmethod
    def import_simp_first():
        from tools.numbers import simp

    @staticmethod
    def import_comp_after_simp():
        try:
            # Attempt to import simp module here if not already imported
            from tools.numbers import simp
        except ImportError as e:
            print(f"Warning: {e}")
            print("Can't run comp before simp. Exiting...")
            raise  # Raise an exception to stop further execution

        # Now that simp is imported, proceed to import comp module
        from tools.numbers import comp

# Create an instance of the ModuleImporter class
module_importer = ModuleImporter()

# Attempting to call functions from comp module before simp module
module_importer.import_comp_after_simp()
