(function() {
    const PUBLIC_KEY = "<PUBLIC_KEY>";
    const vouched = Vouched({
        appId: PUBLIC_KEY,
        
        onInit: ({token, job}) => {
            console.log('initialization');
        },

        onDone: (job)=> {
            console.log("Scanning complete", { job });
        },
        // theme
        theme: {
            name: 'verbose',
        },
    });

    vouched.mount("#vouched-element");
  })();
