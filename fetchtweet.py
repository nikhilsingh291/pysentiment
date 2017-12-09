from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import tweepy
#consumer key, consumer secret, access token, access secret.
ckey="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
csecret="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
atoken="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
asecret="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
f=open('gagloc.txt','w')
##
class listener(StreamListener):
   

    def on_data(self, data):
        all_data=json.loads(data)
        savefile=open('cg.csv','a')
        savefile.write(data)
        savefile.write('\n')
        savefile.close()
##        #print len(all_data)
        #print(all_data["user"]["screen_name"])
        print(all_data["text"])
        print(all_data["user"]["location"])
##        f=open('gagloc.txt','w')
##        f.write(all_data["user"]["location"])
##        f.close()
        return(True)
    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api=tweepy.API(auth)
##user = api.me()
 
##print('Name: ' + user.name)
##print('Location: ' + user.location)
##print('Friends: ' + str(user.friends_count))

##api.update_status('Hola Twitter 2, (checking twitter python api)')
##
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["gddindia"])
print twitterStream










