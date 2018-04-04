import uuid

class Hostpital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, name, allergies, bednum = None):
        if len(self.patients) >= self.capacity:
            return 'We are at capacity and can not take any new patients'
        else:
            self.patients.append(Patient(name, allergies, bednum))
            return 'You are admitted and assigned to bed number {}'.format(bednum)
        return self

    def discharge(self, name):
        pindex = None
        for patient in self.patients:
            if patient.name == name:
                pindex = self.patients.index(patient)
                break
        if pindex == None:
           print 'there are no patients here by that name'
        else:
            self.patients[pindex].bed_number = None
            self.patients.pop(pindex)
        return self

class Patient(object):
    def __init__(self, name, allergies, bednum):
        self.id = str(uuid.uuid4())
        self.name = name
        self.allergies = allergies
        self.bed_number = bednum
