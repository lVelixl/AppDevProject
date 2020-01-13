import random

observations = ['Real', 'Fake']
usernames = ['Jasper', 'Ouk', 'Xavier']

with open('DB_data.dat', 'w') as f:
    for _ in range(4):
        observation = random.choice(observations)
        username = random.choice(usernames)
        password = random.random()

        f.write('{} {} \n'.format(
            observation,
            username,
            password))
