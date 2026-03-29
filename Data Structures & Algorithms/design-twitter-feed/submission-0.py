class Twitter:

    def __init__(self):
        self.tweets = []
        self.tweetCnt = 0
        self.followList = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCnt += 1
        self.tweets.append([self.tweetCnt, userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        feedCnt = 0
        pointer = len(self.tweets) - 1
        following = self.followList[userId] | {userId}
        
        while feedCnt < 10 and pointer >= 0:
            if self.tweets[pointer][1] in following:
                res.append(self.tweets[pointer][2])
                feedCnt += 1
            pointer -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followList[followerId].discard(followeeId)

