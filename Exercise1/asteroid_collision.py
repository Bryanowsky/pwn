class Solution:
    @staticmethod
    def asteroid_collision(asteroids: [int]) -> [int]:
        remaining_asteroids = []

        for asteroid in asteroids:
            # stack not empty and possible collision
            if remaining_asteroids and asteroid < 0 < remaining_asteroids[-1]:
                while remaining_asteroids and 0 < remaining_asteroids[-1] < abs(asteroid):
                    remaining_asteroids.pop()

                if not remaining_asteroids or remaining_asteroids[-1] < 0:
                    remaining_asteroids.append(asteroid)
                elif remaining_asteroids[-1] == abs(asteroid):
                    remaining_asteroids.pop()
            else:
                # stack empty and no possible collision (eg, the same direction top, asteroid)
                remaining_asteroids.append(asteroid)

        return remaining_asteroids


solution = Solution()
print(solution.asteroid_collision([10, 2, -5]))
