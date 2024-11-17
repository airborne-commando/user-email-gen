# Email username gen for both proton mail and outlook (cock.li is optional):

To install and just run for a CLI just run

    python email-gen.py 
    

For HTML just simply do these steps:

    python -m venv venv

</br>

    source venv/bin/activate

</br>

    pip install flask

after that run

    python app.py

For a HTML page


From there you should be given a list of domains to choose from or if you want you can choose a random one from cock.li (optional, see below)

when executed it will display a username and password for outlook, proton and cock.li (optional)

You will still need to solve a captcha for cock.li if you decide to use this.

* Use a VPN, mullvad (if you decided to not edit the webapp and index.html)
* OR if you'd want and trust cock.li, uncomment these lines

app.py:

        # Uncomment this line out for cock.li and comment the next line out if you choose to use cock.li
    
        # return render_template('index.html', domains=d, selected_domains=selected_domains, result=result,
        #                        first_name=random_first_name, last_name=random_last_name, username=random_username)
    
        return render_template('index.html', domains=d, result=result,
                               first_name=random_first_name, last_name=random_last_name, username=random_username)

in index.html

        <form method="post" id="emailForm">
            <div class="domain-list">
    <!-- Uncomment these lines if you want to reuse cock.li again. -->
                <!-- {% for domain in domains %} -->
                <!-- <div class="domain-item"> -->
                    <!-- <input type="checkbox" id="{{ domain }}" name="domains" value="{{ domain }}"  -->
                           <!-- {% if domain in selected_domains %}checked{% endif %}> -->
                    <!-- <label for="{{ domain }}">{{ domain }}</label> -->
                <!-- </div> -->
                <!-- {% endfor %} -->
            </div>
            <!-- <p><small>Select domains you want to generate emails for</small></p> -->
            <input type="submit" value="Generate">
        </form>

......
    
        <!-- Unomment if you want to keep things checked inside the webapp -->
    <!--     <script>
            document.getElementById('emailForm').addEventListener('submit', function(e) {
                var checkboxes = document.querySelectorAll('input[name="domains"]:checked');
                if (checkboxes.length === 0) {
                    e.preventDefault();
                    alert('Please select at least one domain.');
                }
            });
        </script> -->

exmaple output if enabled:
    
    1: cock.li
    2: airmail.cc
    3: firemail.cc
    ...
    Select a domain (1-8) or press Enter for random: 1
    Cock.li: abramduncan6azj@cock.li | (FE[FYb(8xF'H6r}<Ra,9"Jx8.jn;+9gI`ECWoRo&$MRSCkKjmDe,kzMtHc53%t*
    ProtonMail: emoryduncan736@proton.me | ]YX~0~PVoav*{J;u5?\VDTAut*3V_j(~t>CaPS"mV$^';(*d4avs8{kN2+l80yeT
    Outlook: makaisnyderbk3p@outlook.com | K*Zd$ih[h"XgI"zo<Xw(Z<]-:OD*k|OwPje;:o%MJb_</li/7H0ClWC^LZ1b;z1c
    your username is: aurorajugglezetta
    Your password is: 6TD20iN+d!ueP1/|zF\eCy*K\fDOMbZ{f!SSX<i:tteD[nwI%GLGb.:vegfXW^b@


Seems to be a DNS issue; but the alert just seems to be really REALLY stupid.


# Do not abuse this
