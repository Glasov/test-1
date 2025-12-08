
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        specs = [
            "Конфигурация компьютера:",
            f"  CPU: {self.cpu}",
            f"  RAM: {self.ram}",
            f"  Storage: {self.storage}",
            f"  GPU: {self.gpu}"
        ]
        return "\n".join(specs)

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self): pass
    def build_ram(self): pass
    def build_storage(self): pass
    def build_gpu(self): pass

    def get_result(self) -> Computer:
        return self.computer

class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i9-13900K"
    def build_ram(self):
        self.computer.ram = "32GB DDR5"
    def build_storage(self):
        self.computer.storage = "2TB NVMe SSD"
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5-12400"
    def build_ram(self):
        self.computer.ram = "16GB DDR4"
    def build_storage(self):
        self.computer.storage = "512GB SSD"
    def build_gpu(self):
        self.computer.gpu = "Integrated Graphics"


class ComputerAssembler:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()

if __name__ == "__main__":
    print("Сборка игрового компьютера:")
    gaming_builder = GamingComputerBuilder()
    director = ComputerAssembler(gaming_builder)
    director.construct_computer()
    gaming_pc = gaming_builder.get_result()
    print(f"{gaming_pc}\n")

    print("Сборка офисного компьютера:")
    office_builder = OfficeComputerBuilder()
    director = ComputerAssembler(office_builder)
    director.construct_computer()
    office_pc = office_builder.get_result()
    print(office_pc)