class Human:
    def __init__(self, sex: str, nationality: str):
        if not sex or not nationality:
            raise ValueError('Some params are empty!')
        if not isinstance(sex, str) and not isinstance(nationality, str):
            raise TypeError('Invalid params')
        self.sex = sex
        self.nationality = nationality

    def __str__(self):
        return f'Sex: {self.sex}\nNationality: {self.nationality}\n'
