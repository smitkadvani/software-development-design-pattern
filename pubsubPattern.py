class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
    
    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.sendNotification(self.name, event)

from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, channelName, event):
        pass
    
class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name
    
    def sendNotification(self, channelName, event):
        print(f'{self.name} received notification from {channelName}: {event}')
        
channel = YoutubeChannel('smitCodes')
channel.subscribe(YoutubeUser('user1'))
channel.subscribe(YoutubeUser('user2'))
channel.subscribe(YoutubeUser('user3'))

channel.notify('New Video Uploaded')