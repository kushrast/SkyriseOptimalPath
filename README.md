SkyriseOptimalPath
==================

This is a project to find out the optimal robot path for the VEX Skyrise game. Using python, I hope to find an approximate robot strategy to optimize points for time.

The current algorithm is clunky and needs to be simplified but it roughly works like this:

If you are not familiar with VEX Skyrise, the objectives of the game are to stack yellow pegs, called Skyrises, on top of each other as well as drop hollow cubes onto various poles and the Skyrises around the field to earn points.

The first step of the program determines which objectives are left. This is done by evaluating which objectives have a non-zero capacity, meaning that more cubes/skyrises can be scored still.

The second step evaluates whether this activity is Scoring, Stacking, or Picking. Scoring means dropping cubes on a pole/skyrise, Stacking is putting a Skyrise section into the Loader/another Skyrise, and Picking means intaking cubes to either Score or drop cubes on the floor for floor goal points.

After determining this, the maximum TPO (Points:Time) is calculated by figuring out the time necessary to 1. Move to the desired position on the field, 2. Intake any necessary cubes/Skyrises, and 3. Score/Stack the game elements. As you can score multiple cubes at a time, the program finds out whether it is most efficient to score 1,2, or 3 (our max capacity) cubes at that point in time.

Finally, the program compares the TPO's of each activity and chooses the activity with the greatest TPO, which means it is the most efficient, so long as the time required is less than the remaining time in the match. If the required time is greater than the time left, the program iterates through the remaining activities sorted for TPO until a suitable required time is found.

Afterwards, the cube distribution is altered as a result as well as the activity capacities.

_____________________________________________________________________________________________________________________________

This program has a few different use cases. One is to determine the optimal driver strategy for driver skills, a 1 minute single robot trial. Another is to implement two robots and figure out the optimal driver strategy for a co-op run, adjusting the robot values for each robot. Another is to figure out the best strategy against specific other teams/designs by estimating your opponent's capabilities to devise a winning strategy.

In the future, I will try to explore all of these various uses.
