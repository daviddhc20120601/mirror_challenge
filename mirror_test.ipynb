{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# this is simulating the input, "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "r,c,m,n=5,6,1,4\n",
    "pos=[\n",
    "    [2,3],\n",
    "    [1,2],\n",
    "    [2,5],\n",
    "    [4,2],\n",
    "    [5,5]\n",
    "    ]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# in code language , sequence starts with 0 instead of one, so all the cordinates will need to minus one"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_pos(pos_temp):\n",
    "    for i in range(len(pos_temp)):\n",
    "        for j in range(len(pos_temp[i])):\n",
    "            pos_temp[i][j]-=1\n",
    "    print pos_temp\n",
    "    return pos_temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 2], [0, 1], [1, 4], [3, 1], [4, 4]]\n"
     ]
    }
   ],
   "source": [
    "new_pos=convert_pos(pos)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# here i use dict to map all the cordinates to \"L\" or \"R\" which means they are \"/\" or \"\\\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['L', 'R', 'R', 'R', 'R']\n",
      "{'[1, 2]': 'L', '[3, 1]': 'R', '[1, 4]': 'R', '[4, 4]': 'R', '[0, 1]': 'R'}\n"
     ]
    }
   ],
   "source": [
    "mirror_L=[\"L\"]*m\n",
    "mirror_L.extend([\"R\"]*n)\n",
    "print mirror_L\n",
    "new_pos_dict=dict(zip([json.dumps(i) for i in new_pos],mirror_L))\n",
    "print new_pos_dict"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# this is a simple visualizaion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(0,0)\t\\\\\t(0,2)\t(0,3)\t(0,4)\t(0,5)\t\n",
      "\n",
      "(1,0)\t(1,1)\t/////\t(1,3)\t\\\\\t(1,5)\t\n",
      "\n",
      "(2,0)\t(2,1)\t(2,2)\t(2,3)\t(2,4)\t(2,5)\t\n",
      "\n",
      "(3,0)\t\\\\\t(3,2)\t(3,3)\t(3,4)\t(3,5)\t\n",
      "\n",
      "(4,0)\t(4,1)\t(4,2)\t(4,3)\t\\\\\t(4,5)\t\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for r_i in range(r):\n",
    "    for c_i in range(c):\n",
    "        if [r_i,c_i] in pos:\n",
    "            if new_pos_dict[json.dumps([r_i,c_i])] ==\"L\":\n",
    "                print \"/////\\t\",\n",
    "            elif new_pos_dict[json.dumps([r_i,c_i])] ==\"R\":\n",
    "                print \"\\\\\\\\\\t\",\n",
    "        else: print \"(%d,%d)\\t\"%(r_i,c_i),\n",
    "    print \"\\n\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# this is a light class \n",
    "## init:when start, it starts from (0,0) and aim for (0,-2) , i assume the direction to the bigger number is -2, and to the smaller number is -1\n",
    "## ref: reflaction, if it hits \"/\"  or \"\\\", then if it comes from left or right\n",
    "## next_mirror: find the next mirror, go through all the mirrors, if the direction is to smaller \"-1\", then find the closest smaller number, by using distance \n",
    "## this part is not done, yet due to the recent change in the career "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class light:\n",
    "    def init(self):\n",
    "        self.from_loc_now=[0,0]\n",
    "        self.to_loc_now=[0,-2]\n",
    "        return({\"from\":self.from_loc_now,\"to\":self.to_loc_now})\n",
    "    \n",
    "    def ref(self,mirror_loc,left_or_right):\n",
    "        if left_or_right == \"L\" :\n",
    "            if self.from_loc_now[1]<mirror_loc[1]:\n",
    "                self.to_loc_now=[-1,mirror_loc[1]]\n",
    "                self.from_loc_now=mirror_loc\n",
    "            elif self.from_loc_now[1]>mirror_loc[1]:\n",
    "                self.to_loc_now=[-2,mirror_loc[1]]\n",
    "                self.from_loc_now=mirror_loc\n",
    "        elif left_or_right == \"R\" :\n",
    "            if self.from_loc_now[1]<mirror_loc[1]:\n",
    "                self.to_loc_now=[-2,mirror_loc[1]]\n",
    "                self.from_loc_now=mirror_loc\n",
    "            elif self.from_loc_now[1]>mirror_loc[1]:\n",
    "                self.to_loc_now=[-1,mirror_loc[1]]\n",
    "                self.from_loc_now=mirror_loc\n",
    "        return({\"from\":self.from_loc_now,\"to\":self.to_loc_now})\n",
    "                \n",
    "    def next_mirror(self,new_pos_ins):\n",
    "        for i in new_pos_ins:\n",
    "            if self.to_loc_now[0] == -1:\n",
    "                distance = r\n",
    "                if (i[1]==self.to_loc_now[1]) :\n",
    "                    distance_temp = i[0]-self.from_loc_now[0]\n",
    "                    closet_mirror=i\n",
    "                    \n",
    "        return"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# some thoughts:\n",
    "## 1 this version is only brutal force attack , which will be very slow\n",
    "## 2 considering using Genetic Algorithms , which will initial the all non-mirror positions without mirror, then mutate for the best "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
