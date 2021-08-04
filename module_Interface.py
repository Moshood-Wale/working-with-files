from abc import ABC, abstractmethod


class ModuleInterface(ABC):
    @abstractmethod
    def file_opening(self):
        pass
    
    @abstractmethod
    def iterate_files(self):
        pass
    
    @abstractmethod
    def read_whole_file(self):
        pass

    @abstractmethod
    def read_first_two_lines(self):
        pass
    
    @abstractmethod
    def read_last_two_lines(self):
        pass