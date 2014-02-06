
# Script to write letters to editors
# This is a simple hack to mass send letters to editors
# uses this interface http://capwiz.com/

# from the http://www.aauw.org/ site.
# You need to edit these to fill out the forms :
#         MC_signature => "TODO:YOUR SIGNATURE",
#         prefix=>3,
#         first=>                         "TODO:Firstname",
#         last=>                          "TODO:Last Name",
#         email=>                         "TODO:EMAIL",
#         address=>                       "TODO:address",
#         city=>                          "TODO:City",
#         state=>                         "TODO:State",
#         azip=>                          "TODO:Zip",
#         bzip=>                          ""         ,               
#         phone=>                         "TODO:Phone"


use strict;
use warnings;
use WWW::Mechanize;
use LWP::Debug qw(+);
use YAML;


my $subject;
my $body;

sub GetData
{
    my $filename =shift;
    warn "Going to read from $filename\n";
    open IN, "<$filename" or die "cannot open $filename";
    while(<IN>)
    {
        if(!$subject)
        {
            $subject = $_;
        }
        else
        {
            $body .= $_;
        }
    }
    warn "Subject is $subject and body is $body\n";
}



sub process
{
    my $s2=shift;
    my $id=shift;
    my $url = "http://capwiz.com/aauw/mail/compose/?type=ME&alertid=&mediaid=${id}";
    my $mech2 = WWW::Mechanize->new();       
    $mech2->get($url);
    warn $mech2->status();
    warn $mech2->uri();
    
    $mech2->current_form()->strict(1);
    
    my $ret = $mech2->submit_form(
        form_name => "mailapp",
        button => "MC_command",
        fields => {
            MC_command => "Preview Message", # preview
            MC_subject => $subject ,
            MC_message_CUSTOM => $body,
            MC_signature => "TODO:YOUR SIGNATURE",
            prefix=>3,
            first=>                         "TODO:Firstname",
            last=>                          "TODO:Last Name",
            email=>                         "TODO:EMAIL",
            address=>                       "TODO:address",
            city=>                          "TODO:City",
            state=>                         "TODO:State",
            azip=>                          "TODO:Zip",
            bzip=>                          ""         ,               
            phone=>                         "TODO:Phone"
        }
        );

    $ret = $mech2->submit_form(
        form_name => "mailapp",
        button => "MC_command",
        fields => {
            MC_command => "Send Message", # send it
        }
        );
    $mech2->save_content("sent_item_${s2}_${id}.html");
    #  warn $ret->as_string;
    warn "Did $s2 and $id";
    warn $mech2->status();
    warn $mech2->uri();
}


sub Main
{
    # get the parameters
    GetData shift @ARGV;

    my $mech = WWW::Mechanize->new();
    
    my $url ="http://capwiz.com/aauw/dbq/media/";
    
    $mech->get($url);
    
    
    foreach my $s (qw[AK/Alaska AL/Alabama  AS/American Samoa AZ/Arizona AR/Arkansas CA/California CO/Colorado CT/Connecticut DE/Delaware DC/District of Columbia FL/Florida GA/Georgia GU/Guam HI/Hawaii ID/Idaho IL/Illinois IN/Indiana IA/Iowa KS/Kansas KY/Kentucky LA/Louisiana ME/Maine MD/Maryland MA/Massachusetts MI/Michigan MN/Minnesota MS/Mississippi MO/Missouri MT/Montana NE/Nebraska NV/Nevada NH/New Hampshire NJ/New Jersey NM/New Mexico NY/New York NC/North Carolina ND/North Dakota MP/Northern Mariana Islands OH/Ohio OK/Oklahoma OR/Oregon PA/Pennsylvania PR/Puerto Rico RI/Rhode Island SC/South Carolina SD/South Dakota TN/Tennessee TX/Texas UT/Utah VT/Vermont VI/Virgin Islands VA/Virginia WA/Washington WV/West Virginia WI/Wisconsin WY/Wyoming])
    {
        #my $s2 = $s;
        if ($s=~ /^(\w\w)/)
        {
            warn $1;
            my $s2 = $1; #s!\/!\/\w+!g;
            
            $mech->get($url);
            
            $mech->submit_form(
                form_name => "media",
                fields => {
                    "state" => $s2
                }
                );

            my $form = $mech->form_with_fields( qw[mediaid] );
            my @ids = map { $_->{menu}[1]->{value} } @{$form->{inputs}};

            foreach my $id (@ids)
            {
                if (defined($id))
                {
                    process $s2, $id;
                }
            }   
        }
    }

}

Main;
