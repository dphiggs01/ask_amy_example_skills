from ask_amy.utilities.slot_validator import Slot_Validator
import logging

logger = logging.getLogger()


class LIST_OF_PLAYER_NAMES(Slot_Validator):
    VALID = 0  # Passed validation
    MSG_01_TEXT = 1  # Failed Validation

    _valid_values = ['aaron', 'abbie', 'abby', 'abe', 'abigail', 'abraham', 'abram', 'ada', 'adaline', 'adam', 'addy',
                    'agatha', 'aggy', 'agnes', 'aileen', 'al', 'alan', 'albert', 'aldo', 'aldrich', 'alex', 'alexander',
                    'alexandra', 'alfonse', 'alfred', 'alfreda', 'alice', 'alicia', 'allan', 'allen', 'allie', 'almena',
                    'alonzo', 'amanda', 'amber', 'amelia', 'amy', 'anderson', 'andrea', 'andrew', 'andy', 'angela',
                    'ann', 'anne', 'annie', 'anthony', 'antoinette', 'antonia', 'ara', 'arabella', 'arabelle',
                    'archibald', 'archie', 'arlene', 'arly', 'art', 'arthur', 'ashley', 'augusta', 'augustina',
                    'augustine', 'augustus', 'babs', 'barbara', 'barbie', 'barnabas', 'barney', 'bart', 'bartholomew',
                    'bea', 'beatrice', 'becca', 'becky', 'belinda', 'bella', 'belle', 'ben', 'benedict', 'benjamin',
                    'benjy', 'bennie', 'bernard', 'berny', 'bert', 'bertha', 'bess', 'beth', 'betsy', 'betty', 'bill',
                    'billy', 'birdie', 'birtie', 'bob', 'bobbie', 'bobby', 'brad', 'bradford', 'brandon', 'brian',
                    'brit', 'brittany', 'broderick', 'brody', 'cal', 'calvin', 'camile', 'cammie', 'carl', 'carol',
                    'carolann', 'caroline', 'carolyn', 'cassandra', 'cassie', 'catherine', 'cathleen', 'cathy',
                    'charles', 'charlie', 'chester', 'chet', 'chrintina', 'chrintine', 'chris', 'christa', 'christian',
                    'christina', 'christine', 'christopher', 'chuck', 'cinderlla', 'cindy', 'clara', 'clarissa',
                    'cliff', 'clifford', 'clifton', 'connie', 'constance', 'cornelius', 'crissy', 'crystal', 'curt',
                    'curtis', 'cy', 'cynthia', 'cyrus', 'dan', 'daniel', 'danielle', 'danny', 'darlene', 'dave',
                    'davey', 'david', 'deb', 'debbie', 'deborah', 'debra', 'dee', 'del', 'delbert', 'della', 'delores',
                    'dennie', 'dennis', 'dennison', 'denny', 'derick', 'dick', 'dolly', 'dom', 'domenic', 'dominico',
                    'don', 'donald', 'donato', 'donnie', 'donny', 'dora', 'dorothy', 'dot', 'dottie', 'dotty', 'drew',
                    'ed', 'eddie', 'eddy', 'edgar', 'edie', 'edith', 'edmond', 'edmund', 'eduardo', 'edward', 'edwin',
                    'edye', 'edyth', 'edythe', 'elaine', 'elbert', 'eldora', 'eleanor', 'elias', 'elizabeth', 'ella',
                    'ellen', 'elwood', 'emeline', 'emily', 'emma', 'eric', 'erica', 'erin', 'estella', 'eugene', 'eve',
                    'faith', 'fay', 'ferdinand', 'flo', 'flora', 'florence', 'fran', 'frances', 'francie', 'francine',
                    'francis', 'frank', 'frankie', 'franklin', 'frannie', 'franny', 'fred', 'freda', 'freddie',
                    'freddy', 'frederick', 'fredericka', 'frieda', 'gabby', 'gabe', 'gabriel', 'gabriella', 'gabrielle',
                    'gail', 'gene', 'genevieve', 'geoff', 'geoffrey', 'george', 'georgine', 'gerald', 'geraldine',
                    'gerrie', 'gerry', 'gertie', 'gertrude', 'gil', 'gilbert', 'gina', 'greg', 'gretta', 'gus', 'gwen',
                    'gwendolyn', 'hal', 'hank', 'hannah', 'harold', 'harriet', 'harry', 'hattie', 'heather', 'henny',
                    'henrietta', 'henry', 'herb', 'herbert', 'hester', 'hetty', 'hipsbibah', 'hipsie', 'hubert', 'hugh',
                    'iggy', 'ignatius', 'irene', 'isabel', 'isabella', 'isabelle', 'isadora', 'isadore', 'issy', 'izzy',
                    'jacob', 'jake', 'james', 'jamie', 'jan', 'janet', 'jason', 'jay', 'jean', 'jeb', 'jebadiah',
                    'jeff', 'jefferson', 'jeffrey', 'jenn', 'jennie', 'jennifer', 'jenny', 'jeremiah', 'jeremy',
                    'jerry', 'jessica', 'jessie', 'jim', 'jimmie', 'jimmy', 'jo', 'joan', 'joann', 'joanna', 'joanne',
                    'jody', 'joe', 'joey', 'johann', 'johanna', 'johannah', 'john', 'jon', 'jonathan', 'joseph',
                    'josey', 'josh', 'joshua', 'josophine', 'joy', 'joyce', 'judith', 'judy', 'julia', 'julie',
                    'justin', 'kate', 'katelin', 'katelyn', 'katherine', 'kathleen', 'kathryn', 'kathy', 'katie',
                    'katy', 'kay', 'kaye', 'kelly', 'ken', 'kenneth', 'kenny', 'kevin', 'kim', 'kimberley', 'kimberly',
                    'kristen', 'kristin', 'kristy', 'kyle', 'lamont', 'larry', 'latisha', 'laura', 'lauren', 'laurence',
                    'lawrence', 'lee', 'lena', 'lenny', 'lenora', 'leo', 'leon', 'leonard', 'les', 'lester', 'libby',
                    'lillian', 'lilly', 'linda', 'lindsay', 'lindsey', 'lisa', 'liz', 'lizzie', 'lois', 'loretta',
                    'lorie', 'lorraine', 'lou', 'louis', 'louise', 'lucias', 'lucinda', 'lucy', 'luke', 'lynn', 'maddy',
                    'madeline', 'madelyn', 'madge', 'madie', 'magdelina', 'maggie', 'maggy', 'mandy', 'marcus',
                    'margaret', 'margaretta', 'marge', 'margie', 'margy', 'marjorie', 'mark', 'martin', 'martina',
                    'marty', 'marv', 'marvin', 'mary', 'mathew', 'matilda', 'matt', 'matthew', 'maud', 'megan', 'mel',
                    'melinda', 'melissa', 'merv', 'mervin', 'michael', 'michelle', 'mick', 'mickey', 'mike', 'mindy',
                    'minnie', 'missy', 'mitch', 'mitchell', 'napoleon', 'nat', 'nate', 'nathan', 'nathaniel', 'neil',
                    'newt', 'newton', 'nicholas', 'nick', 'nickie', 'nicole', 'nora', 'norbert', 'obediah', 'obie',
                    'oliver', 'ollie', 'oswald', 'ozzy', 'pat', 'patricia', 'patrick', 'patsy', 'patty', 'paulina',
                    'peggy', 'penelope', 'penny', 'pete', 'peter', 'philip', 'phillip', 'philpoint', 'pointlucas',
                    'pointmonty', 'pointsolomon', 'pointveronica', 'polly', 'prescott', 'priscilla', 'prissy',
                    'prudence', 'prudy', 'rachel', 'randolph', 'randy', 'ray', 'raymond', 'reba', 'rebecca',
                    'reggie', 'regina', 'reginald', 'rena', 'reuben', 'ricardo', 'rich', 'richard', 'richie', 'rick',
                    'ricky', 'rob', 'robby', 'robert', 'roberta', 'roberto', 'rod', 'ron', 'ronald', 'ronnie', 'ronny',
                    'rosabel', 'rosabella', 'rosaenn', 'rosaenna', 'rosalyn', 'rose', 'roseann', 'roseanna', 'roxanna',
                    'roxanne', 'roz', 'rube', 'rudolph', 'rudy', 'russ', 'russell', 'rusty', 'ryan', 'sal', 'sam',
                    'samantha', 'sammy', 'samuel', 'sandra', 'sandy', 'sara', 'sarah', 'scott', 'scotty', 'sean',
                    'shelly', 'shelton', 'sherry', 'shirley', 'sly', 'stella', 'steph', 'stephanie', 'stephen', 'steve',
                    'steven', 'sue', 'sullivan', 'sully', 'susan', 'susannah', 'susie', 'sylvester', 'tabby', 'tabitha',
                    'ted', 'teddy', 'terence', 'teresa', 'terry', 'tess', 'tessa', 'tessie', 'thad', 'thaddeus', 'theo',
                    'theodore', 'theresa', 'thom', 'thomas', 'tiffany', 'tilla', 'tim', 'timmy', 'timothy', 'tina',
                    'tish', 'tisha', 'tobias', 'toby', 'tom', 'tommy', 'tony', 'tori', 'torie', 'torri', 'torrie',
                    'tory', 'trisha', 'trixie', 'trudy', 'val', 'valeri', 'valerie', 'van', 'vanessa', 'vanna', 'vic',
                    'vicki', 'vickie', 'vicky', 'victor', 'victoria', 'vin', 'vince', 'vincent', 'vincenzo',
                    'vincenzon', 'vinnie', 'vinson', 'waldo', 'wendy', 'wilber', 'wilbur', 'wilhelmina', 'will',
                    'william', 'willie', 'wilma', 'wilson', 'winnie', 'winnifred', 'winny', 'woody', 'zach',
                    'zachariah', 'zachary']

    def is_valid_value(self, value):
        logger.debug("LIST_OF_PLAYER_NAMES.is_valid_value {}".format(value))
        status_code = LIST_OF_PLAYER_NAMES.MSG_01_TEXT
        if isinstance(value, str):
            if value.lower() in LIST_OF_PLAYER_NAMES._valid_values:
                status_code = LIST_OF_PLAYER_NAMES.VALID
        return status_code