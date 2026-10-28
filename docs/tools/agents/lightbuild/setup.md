---
title: https://developer.android.com/tools/agents/lightbuild/setup
url: https://developer.android.com/tools/agents/lightbuild/setup
source: md.txt
---










<!doctype html>
<html 
      lang="en"
      dir="ltr">
  <head>
    <meta name="google-signin-client-id" content="721724668570-nbkv1cfusk7kk4eni4pjvepaus73b13t.apps.googleusercontent.com"><meta name="google-signin-scope"
          content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award https://www.googleapis.com/auth/devprofiles.full_control.firstparty"><meta property="og:site_name" content="Android Developers">
    <meta property="og:type" content="website"><meta name="theme-color" content="#34a853"><meta charset="utf-8">
    <meta content="IE=Edge" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

    <link rel="manifest" href="/_pwa/android/manifest.json"
          crossorigin="use-credentials">
    <link rel="preconnect" href="//www.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="//www.google-analytics.com" crossorigin><link rel="stylesheet" href="//fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Text:400,400italic,500,500italic,600,600italic,700,700italic|Roboto+Mono:400,500,700&display=swap">
      <link rel="stylesheet"
            href="//fonts.googleapis.com/css2?family=Material+Icons&family=Material+Symbols+Outlined&display=block"><link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/css/app.css">
      
        <link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/css/dark-theme.css" disabled>
      <link rel="shortcut icon" href="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/favicon.svg">
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/touchicon-180.png"><link rel="canonical" href="https://developer.android.com/studio/intro"><link rel="search" type="application/opensearchdescription+xml"
            title="Android Developers" href="https://developer.android.com/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://developer.android.com/studio/intro" /><link rel="alternate" hreflang="x-default" href="https://developer.android.com/studio/intro" /><link rel="alternate" hreflang="ar"
          href="https://developer.android.com/studio/intro?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://developer.android.com/studio/intro?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://developer.android.com/studio/intro?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://developer.android.com/studio/intro?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://developer.android.com/studio/intro?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://developer.android.com/studio/intro?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://developer.android.com/studio/intro?hl=de" /><link rel="alternate" hreflang="he"
          href="https://developer.android.com/studio/intro?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://developer.android.com/studio/intro?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://developer.android.com/studio/intro?hl=id" /><link rel="alternate" hreflang="it"
          href="https://developer.android.com/studio/intro?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://developer.android.com/studio/intro?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://developer.android.com/studio/intro?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://developer.android.com/studio/intro?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://developer.android.com/studio/intro?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://developer.android.com/studio/intro?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://developer.android.com/studio/intro?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://developer.android.com/studio/intro?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://developer.android.com/studio/intro?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://developer.android.com/studio/intro?hl=vi" /><title>Meet Android Studio &nbsp;|&nbsp; Android Developers</title>

<meta property="og:title" content="Meet Android Studio &nbsp;|&nbsp; Android Developers"><meta name="description" content="Android Studio is the official Integrated Development Environment (IDE) for Android app development, based on IntelliJ IDEA.">
  <meta property="og:description" content="Android Studio is the official Integrated Development Environment (IDE) for Android app development, based on IntelliJ IDEA."><meta property="og:url" content="https://developer.android.com/studio/intro"><meta property="og:image" content="https://developer.android.com/static/images/social/android-developers.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675"><meta property="og:locale" content="en"><meta name="twitter:card" content="summary_large_image"><script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    
    "headline": "Meet Android Studio"
  }
</script><script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{
      "@type": "ListItem",
      "position": 1,
      "name": "Android Studio",
      "item": "https://developer.android.com/studio"
    },{
      "@type": "ListItem",
      "position": 2,
      "name": "Meet Android Studio",
      "item": "https://developer.android.com/studio/intro"
    }]
  }
  </script>
  

  

  

  

  
<meta name="keywords" content="Android Studio, IDE, Gradle, debugging, profiling, lint, project structure, build system, Android development">

    </head>
  <body class="color-scheme--light"
        template="page"
        theme="android-theme"
        type="article"
        
        appearance
        
        layout="docs"
        
        
        
        
        
        display-toc
        pending>
  
    <devsite-progress type="indeterminate" id="app-progress"></devsite-progress>
  
  
    <a href="#main-content" class="skip-link button">
      
      Skip to main content
    </a>
    <section class="devsite-wrapper">
      <devsite-cookie-notification-bar></devsite-cookie-notification-bar>
        <devsite-header role="banner">
  
    





















<div class="devsite-header--inner" data-nosnippet>
  <div class="devsite-top-logo-row-wrapper-wrapper">
    <div class="devsite-top-logo-row-wrapper">
      <div class="devsite-top-logo-row">
        <button type="button" id="devsite-hamburger-menu"
          class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
          data-category="Site-Wide Custom Events"
          data-label="Navigation menu button"
          visually-hidden
          aria-label="Open menu">
        </button>
        
<div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="androidDevelopers" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/lockup-dark-theme.png"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/lockup.png" class="devsite-site-logo" alt="Android Developers">
  </picture>
  
</a>



</div>
        <div class="devsite-top-logo-row-middle">
          <div class="devsite-header-upper-tabs">
            
              
              
  <devsite-tabs class="upper-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Upper tabs">
      
        
          <tab class="devsite-dropdown
    devsite-dropdown-full
    
    
    ">
  
    <a href="https://developer.android.com/get-started"
    class="devsite-tabs-content gc-analytics-event android-dropdown-tab"
      track-metadata-eventdetail="https://developer.android.com/get-started"
    
       track-type="nav"
       track-metadata-position="nav - essentials"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Essentials"
         
           track-name="essentials"
         
       >
    Essentials
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Essentials"
         track-type="nav"
         track-metadata-eventdetail="https://developer.android.com/get-started"
         track-metadata-position="nav - essentials"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Essentials"
          
            track-name="essentials"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-dropdown-primary android-dropdown-ai">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Build AI experiences</li>
              
              
                <li class="devsite-nav-description">Build AI-powered Android apps with Gemini APIs and more.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/ai"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/ai"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build ai experiences"
                     
                     tooltip
                  
                    
                     class="button button-primary"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Get started
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-launch">
              
                <li class="devsite-nav-title" role="heading" tooltip>Get started</li>
              
              
                <li class="devsite-nav-description">Create your first app. Use Compose for UI and adaptive app development to support multiple device form factors.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/get-started/overview"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/get-started/overview"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get started"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Hello, world!
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/adaptive-apps"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/adaptive-apps"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get started"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Adaptive apps
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/compose"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/compose"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get started"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Compose for UI
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/studio"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/studio"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get started"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      AI-powered IDE
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://google.play/business/guides/play-commerce/"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://google.play/business/guides/play-commerce/"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get started"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Monetization with Play ↗️
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/developer-verification"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/developer-verification"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get started"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Developer Verification
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/registered-app-stores"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/registered-app-stores"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get started"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Registered App Stores
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-multiple-screens">
              
                <li class="devsite-nav-title" role="heading" tooltip>Optimize by form factor</li>
              
              
                <li class="devsite-nav-description">Build apps that optimize the user experience on phones, tablets, foldables, cars, XR, and more.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/phones-tablets-foldables"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/phones-tablets-foldables"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="optimize by form factor"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Phones, tablets, foldables
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/cars"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/cars"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="optimize by form factor"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android for Cars
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/tv"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/tv"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="optimize by form factor"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android TV
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/xr"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/xr"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="optimize by form factor"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android XR
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/googlebook"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/googlebook"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="optimize by form factor"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Googlebook
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/chrome-os"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/chrome-os"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="optimize by form factor"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      ChromeOS
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/wear"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/wear"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="optimize by form factor"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Wear OS
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-platform">
              
                <li class="devsite-nav-title" role="heading" tooltip>Build by category</li>
              
              
                <li class="devsite-nav-description">Learn to build for your use case by following Google&#39;s prescriptive and opinionated guidance.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/games"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/games"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build by category"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Games
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/media"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/media"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build by category"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Camera & media
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/social-and-messaging"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/social-and-messaging"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build by category"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Social & messaging
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/health-and-fitness"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/health-and-fitness"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build by category"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Health & fitness
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/productivity"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/productivity"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build by category"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Productivity
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/work/overview"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/work/overview"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build by category"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Enterprise apps
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-stars">
              
                <li class="devsite-nav-title" role="heading" tooltip>Get the latest</li>
              
              
                <li class="devsite-nav-description">Stay in touch with the latest releases throughout the year, join our preview programs, and give us your feedback.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/latest-updates"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/latest-updates"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get the latest"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Latest updates
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/latest-updates/experimental"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/latest-updates/experimental"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get the latest"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Experimental updates
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/studio/preview"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/studio/preview"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get the latest"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android Studio preview
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/jetpack/androidx/versions"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/jetpack/androidx/versions"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get the latest"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Jetpack & Compose libraries
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/training/wearables/versions/latest"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/training/wearables/versions/latest"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get the latest"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Wear OS releases
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design-for-safety/privacy-sandbox"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design-for-safety/privacy-sandbox"
                     track-metadata-position="nav - essentials"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="get the latest"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Privacy Sandbox ↗️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    devsite-dropdown-full
    
    
    ">
  
    <a href="https://developer.android.com/design"
    class="devsite-tabs-content gc-analytics-event android-dropdown-tab"
      track-metadata-eventdetail="https://developer.android.com/design"
    
       track-type="nav"
       track-metadata-position="nav - design &amp; plan"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Design &amp; Plan"
         
           track-name="design &amp; plan"
         
       >
    Design &amp; Plan
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Design &amp; Plan"
         track-type="nav"
         track-metadata-eventdetail="https://developer.android.com/design"
         track-metadata-position="nav - design &amp; plan"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Design &amp; Plan"
          
            track-name="design &amp; plan"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-dropdown-primary android-dropdown-mad">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Excellent Experiences</li>
              
              
                <li class="devsite-nav-description">Build the best experiences for your best users.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/quality/excellent"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/quality/excellent"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="excellent experiences"
                     
                     tooltip
                  
                    
                     class="button button-primary"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Learn more
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-layout">
              
                <li class="devsite-nav-title" role="heading" tooltip>UI Design</li>
              
              
                <li class="devsite-nav-description">Design a beautiful user interface using Android best practices.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Design for Android
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/mobile"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/mobile"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Mobile
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/desktop"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/desktop"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Desktop experiences
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/xr"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/xr"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      XR Headsets & XR Glasses
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/ai-glasses"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/ai-glasses"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      AI Glasses
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/widget"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/widget"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Widgets
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/wear"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/wear"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Wear OS
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/tv"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/tv"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android TV
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/design/ui/cars"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/design/ui/cars"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="ui design"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android for Cars
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-design">
              
                <li class="devsite-nav-title" role="heading" tooltip>Architecture</li>
              
              
                <li class="devsite-nav-description">Design robust, testable, and maintainable app logic and services.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/topic/architecture/intro"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/topic/architecture/intro"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="architecture"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Introduction
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/topic/libraries/view-binding"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/topic/libraries/view-binding"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="architecture"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Libraries
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/navigation/navigation-principles"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/navigation/navigation-principles"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="architecture"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Navigation
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/topic/modularization"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/topic/modularization"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="architecture"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Modularization
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/training/testing/fundamentals"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/training/testing/fundamentals"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="architecture"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Testing
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/kotlin/multiplatform"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/kotlin/multiplatform"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="architecture"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Kotlin Multiplatform
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-vitals">
              
                <li class="devsite-nav-title" role="heading" tooltip>Quality</li>
              
              
                <li class="devsite-nav-description">Plan for app quality and align with Play store guidelines.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/quality"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/quality"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="quality"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Overview
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/quality/core-value"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/quality/core-value"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="quality"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Core value
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/quality/user-experience"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/quality/user-experience"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="quality"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      User experience
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/topics/ui/accessibility"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/topics/ui/accessibility"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="quality"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Accessibility
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/quality/technical"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/quality/technical"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="quality"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Technical quality
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/quality/excellent"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/quality/excellent"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="quality"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Excellent Experiences
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-security-2">
              
                <li class="devsite-nav-title" role="heading" tooltip>Security</li>
              
              
                <li class="devsite-nav-description">Safeguard users against threats and ensure a secure Android experience.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/security"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/security"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="security"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Overview
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/privacy"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/privacy"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="security"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Privacy
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/privacy#app-permissions"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/privacy#app-permissions"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="security"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Permissions
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/identity"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/identity"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="security"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Identity
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/security/fraud-prevention"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/security/fraud-prevention"
                     track-metadata-position="nav - design &amp; plan"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="security"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Fraud prevention
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    devsite-dropdown-full
    devsite-active
    
    ">
  
    <a href="https://developer.android.com/develop"
    class="devsite-tabs-content gc-analytics-event android-dropdown-tab"
      track-metadata-eventdetail="https://developer.android.com/develop"
    
       track-type="nav"
       track-metadata-position="nav - develop"
       track-metadata-module="primary nav"
       aria-label="Develop, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Develop"
         
           track-name="develop"
         
       >
    Develop
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Develop"
         track-type="nav"
         track-metadata-eventdetail="https://developer.android.com/develop"
         track-metadata-position="nav - develop"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Develop"
          
            track-name="develop"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-dropdown-primary android-dropdown-studio">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Build more with agents in Android</li>
              
              
                <li class="devsite-nav-description">Turn prompts into real Android experiences using your favorite agents.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/ai-in-android"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/ai-in-android"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build more with agents in android"
                     
                     tooltip
                  
                    
                     class="button button-primary"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Learn more
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/cli"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/cli"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build more with agents in android"
                     
                     tooltip
                  
                    
                     class="button button-white"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Get Android CLI
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-flag">
              
                <li class="devsite-nav-title" role="heading" tooltip>Core areas</li>
              
              
                <li class="devsite-nav-description">Get the samples and docs for the features you need.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/samples"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/samples"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="core areas"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Samples
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/multidevice"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/multidevice"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="core areas"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Multidevice support
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/develop/ui"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/develop/ui"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="core areas"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      User interfaces
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/develop/background-work"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/develop/background-work"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="core areas"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Background work
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/topics/data"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/topics/data"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="core areas"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Data and files
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/develop/connectivity"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/develop/connectivity"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="core areas"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Connectivity
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/develop#core-areas"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/develop#core-areas"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="core areas"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      All core areas ⤵️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-tools-2">
              
                <li class="devsite-nav-title" role="heading" tooltip>Tools and workflow</li>
              
              
                <li class="devsite-nav-description">Use the IDE to write and build your app, or create your own pipeline.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/studio/write"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/studio/write"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Write and debug code
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/build/gradle-build-overview"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/build/gradle-build-overview"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Build projects
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/training/testing"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/training/testing"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Test your app
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/topic/performance/overview"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/topic/performance/overview"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Performance
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/tools"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/tools"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Command-line tools
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/reference/tools/gradle-api"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/reference/tools/gradle-api"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Gradle plugin API
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/bench"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/bench"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android Bench
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/ai-tools"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/ai-tools"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools and workflow"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Build with agents
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-multiple-screens">
              
                <li class="devsite-nav-title" role="heading" tooltip>Device tech</li>
              
              
                <li class="devsite-nav-description">Write code for form factors. Connect devices and share data.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/phones-tablets-foldables"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/phones-tablets-foldables"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Phones, tablets, foldables
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/googlebook"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/googlebook"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Googlebook
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/chrome-os"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/chrome-os"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      ChromeOS
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/training/cars"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/training/cars"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android for Cars
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/training/tv"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/training/tv"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android TV
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/develop/xr"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/develop/xr"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android XR
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/training/wearables"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/training/wearables"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Wear OS
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/health-and-fitness/guides"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/health-and-fitness/guides"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android Health
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/develop/better-together"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/develop/better-together"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Better Together
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/develop#devices"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/develop#devices"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="device tech"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      All devices ⤵️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-core-library">
              
                <li class="devsite-nav-title" role="heading" tooltip>Libraries</li>
              
              
                <li class="devsite-nav-description">Browse API reference documentation with all the details.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/reference/packages"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/reference/packages"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android platform
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/jetpack/androidx/explorer"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/jetpack/androidx/explorer"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Jetpack libraries
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/jetpack/androidx/releases/compose"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/jetpack/androidx/releases/compose"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Compose libraries
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developers.google.com/android/reference/packages"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developers.google.com/android/reference/packages"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google Play services ↗️
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://play.google.com/sdks"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://play.google.com/sdks"
                     track-metadata-position="nav - develop"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google Play SDK index ↗️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    devsite-dropdown-full
    
    
    ">
  
    <a href="https://developer.android.com/distribute"
    class="devsite-tabs-content gc-analytics-event android-dropdown-tab"
      track-metadata-eventdetail="https://developer.android.com/distribute"
    
       track-type="nav"
       track-metadata-position="nav - google play"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Google Play"
         
           track-name="google play"
         
       >
    Google Play
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Google Play"
         track-type="nav"
         track-metadata-eventdetail="https://developer.android.com/distribute"
         track-metadata-position="nav - google play"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Google Play"
          
            track-name="google play"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-dropdown-primary android-dropdown-play">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Play Console</li>
              
              
                <li class="devsite-nav-description">Publish your app or game and grow your business on Google Play.
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://play.google.com/console"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://play.google.com/console"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="play console"
                     
                     tooltip
                  
                    
                     class="button button-white"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Go to Play Console
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://google.play/business/"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://google.play/business/"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="play console"
                     
                     tooltip
                  
                    
                     class="button button-primary"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Learn more ↗️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-google-play">
              
                <li class="devsite-nav-title" role="heading" tooltip>Fundamentals</li>
              
              
                <li class="devsite-nav-description">Learn how to engage users, monitize, and secure your app.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/distribute/play-billing"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/distribute/play-billing"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="fundamentals"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Monetization
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/google/play/integrity"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/google/play/integrity"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="fundamentals"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Integrity
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/google/play/vitals"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/google/play/vitals"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="fundamentals"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android vitals
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/distribute/play-policies"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/distribute/play-policies"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="fundamentals"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Policies
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://google.play/business/programs"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://google.play/business/programs"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="fundamentals"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Programs ↗️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-game-controller">
              
                <li class="devsite-nav-title" role="heading" tooltip>Games Dev Center</li>
              
              
                <li class="devsite-nav-description">Develop and deliver games. Get tools, downloads, and samples.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/games"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/games"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="games dev center"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Overview
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/playcore/asset-delivery"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/playcore/asset-delivery"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="games dev center"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Asset Delivery
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/games/pgs/overview"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/games/pgs/overview"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="games dev center"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Games Services
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/games/playgames/overview"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/games/playgames/overview"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="games dev center"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Games on PC
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/games/guidelines"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/games/guidelines"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="games dev center"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Level Up guidelines
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/distribute"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/distribute"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="games dev center"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      All Play guides ⤵️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-core-library">
              
                <li class="devsite-nav-title" role="heading" tooltip>Libraries</li>
              
              
                <li class="devsite-nav-description">Browse API reference documentation with all the details.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/playcore/feature-delivery"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/playcore/feature-delivery"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Feature Delivery
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/playcore/in-app-updates"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/playcore/in-app-updates"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play In-app Updates
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/playcore/in-app-review"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/playcore/in-app-review"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play In-app Reviews
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/google/play/installreferrer"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/google/play/installreferrer"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Install Referrer
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developers.google.com/android/reference/packages"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developers.google.com/android/reference/packages"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google Play services ↗️
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://play.google.com/sdks"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://play.google.com/sdks"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google Play SDK index ↗️
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/distribute"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/distribute"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="libraries"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      All Play libraries ⤵️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       android-dropdown-section-icon android-dropdown-section-icon-tools-2">
              
                <li class="devsite-nav-title" role="heading" tooltip>Tools &amp; resources</li>
              
              
                <li class="devsite-nav-description">Tools for publishing, promoting, and managing your app.</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/guide/app-bundle"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/guide/app-bundle"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools &amp; resources"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Android App Bundles
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/distribute/marketing-tools"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/distribute/marketing-tools"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools &amp; resources"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Brand & marketing
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developers.google.com/android-publisher/api-ref/rest"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developers.google.com/android-publisher/api-ref/rest"
                     track-metadata-position="nav - google play"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="tools &amp; resources"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Play Console APIs ↗️
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    devsite-dropdown-full
    
    
    ">
  
    <a href="https://developer.android.com/blog"
    class="devsite-tabs-content gc-analytics-event android-dropdown-tab android-dropdown-tab-blog android-nav-icon-new-blog"
      track-metadata-eventdetail="https://developer.android.com/blog"
    
       track-type="nav"
       track-metadata-position="nav - blog"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Blog"
         
           track-name="blog"
         
       >
    Blog
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Blog"
         track-type="nav"
         track-metadata-eventdetail="https://developer.android.com/blog"
         track-metadata-position="nav - blog"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Blog"
          
            track-name="blog"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-dropdown-primary android-dropdown-blog">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>the Android Developer&#39;s Blog</li>
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/latest"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/latest"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="the android developer&#39;s blog"
                     
                     tooltip
                  
                    
                     class="button button-primary"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Read the latest
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/authors"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/authors"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="the android developer&#39;s blog"
                     
                     tooltip
                  
                    
                     class="button button-white"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Explore the authors →
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-blog-categories-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Explore categories</li>
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/categories/product-news"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/categories/product-news"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="explore categories"
                     
                     tooltip
                  
                    
                     class="android-nav-icon-product-news"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Product News
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Stay in the loop with the latest updates, feature releases, and behind-the-scenes looks at how we’re evolving.
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/categories/community"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/categories/community"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="explore categories"
                     
                     tooltip
                  
                    
                     class="android-nav-icon-community"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Community
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Discover stories from our users, spotlight features, and the collaborative projects that bring us all together.
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-blog-categories-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/categories/how-tos"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/categories/how-tos"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  
                    
                     class="android-nav-icon-how-tos"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      How-tos
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      From quick tips to deep-dive tutorials, these step-by-step guides are designed to help you work smarter and faster.
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/categories/case-studies"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/categories/case-studies"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  
                    
                     class="android-nav-icon-case-studies"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Case Studies
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Real-world results from real-world users. Explore how different teams use our tools to achieve their goals.
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    android-dropdown android-blog-categories-dropdown">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/categories/events-and-programs"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/categories/events-and-programs"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  
                    
                     class="android-nav-icon-events-and-programs"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Events & Programs
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Get the details on upcoming webinars, workshops, meetups, and special initiatives designed to help you grow.
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://developer.android.com/blog/categories/documentation"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://developer.android.com/blog/categories/documentation"
                     track-metadata-position="nav - blog"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  
                    
                     class="android-nav-icon-documentation"
                    
                  >
                    
                    <div class="devsite-nav-item-title">
                      Documentation
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Access detailed manuals, API references, and technical specifications to help you build and integrate with confidence.
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
    </nav>

  </devsite-tabs>

            
           </div>
          
<devsite-search
    enable-signin
    enable-search
    enable-suggestions
      enable-query-completion
    
    
    project-name="Android Studio"
    tenant-name="Android Developers"
    
    
    
    
    
    >
  <form class="devsite-search-form" action="https://developer.android.com/s/results" method="GET">
    <div class="devsite-search-container">
      <button type="button"
              search-open
              class="devsite-search-button devsite-header-icon-button button-flat material-icons"
              
              aria-label="Open search"></button>
      <div class="devsite-searchbox">
        <input
          aria-activedescendant=""
          aria-autocomplete="list"
          
          aria-label="Search"
          aria-expanded="false"
          aria-haspopup="listbox"
          autocomplete="off"
          class="devsite-search-field devsite-search-query"
          name="q"
          
          placeholder="Search"
          role="combobox"
          type="text"
          value=""
          >
          <div class="devsite-search-image material-icons" aria-hidden="true">
            
          </div>
          <div class="devsite-search-shortcut-icon-container" aria-hidden="true">
            <kbd class="devsite-search-shortcut-icon">/</kbd>
          </div>
      </div>
    </div>
  </form>
  <button type="button"
          search-close
          class="devsite-search-button devsite-header-icon-button button-flat material-icons"
          
          aria-label="Close search"></button>
</devsite-search>

        </div>

        

          

          

          

          <devsite-appearance-selector></devsite-appearance-selector>

          
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="id"
        >Indonesia</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="it"
        >Italiano</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pl"
        >Polski</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="vi"
        >Tiếng Việt</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="tr"
        >Türkçe</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ru"
        >Русский</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ar"
        >العربيّة</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fa"
        >فارسی</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="hi"
        >हिंदी</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="bn"
        >বাংলা</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="th"
        >ภาษาไทย</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_tw"
        >中文 – 繁體</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>


          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="https://developer.android.com/studio"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Android Studio"
    >
  Android Studio
</a>
          

        

        
          <devsite-user 
                        
                        
                          enable-profiles
                        
                        
                        id="devsite-user">
            
              
              <span class="button devsite-top-button" aria-hidden="true" visually-hidden>Sign in</span>
            
          </devsite-user>
        
        
        
      </div>
    </div>
  </div>



  <div class="devsite-collapsible-section
    ">
    <div class="devsite-header-background">
      
        
          <div class="devsite-product-id-row"
           >
            <div class="devsite-product-description-row">
              
                
                <div class="devsite-product-id">
                  
                  
                  
                    <ul class="devsite-breadcrumb-list"
  >
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://developer.android.com/studio"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Lower Header"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Android Studio"
      
    >
    
          Android Studio
        
  </a>
  
      
    
  </li>
  
</ul>
                </div>
                
              
              
            </div>
            
          </div>
          
        
      
      
        <div class="devsite-doc-set-nav-row">
          
          
            
            
  <devsite-tabs class="lower-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Lower tabs">
      
        
          <tab  >
            
    <a href="https://developer.android.com/studio"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://developer.android.com/studio"
    
       track-type="nav"
       track-metadata-position="nav - download"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Download"
         
           track-name="download"
         
       >
    Download
  
    </a>
    
  
          </tab>
        
      
        
          <tab  class="devsite-active">
            
    <a href="https://developer.android.com/studio/intro"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://developer.android.com/studio/intro"
    
       track-type="nav"
       track-metadata-position="nav - ide guides"
       track-metadata-module="primary nav"
       aria-label="IDE guides, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: IDE guides"
         
           track-name="ide guides"
         
       >
    IDE guides
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://developer.android.com/ai-in-android"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://developer.android.com/ai-in-android"
    
       track-type="nav"
       track-metadata-position="nav - ai in android studio"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: AI in Android Studio"
         
           track-name="ai in android studio"
         
       >
    AI in Android Studio
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://developer.android.com/tools/agents"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://developer.android.com/tools/agents"
    
       track-type="nav"
       track-metadata-position="nav - agent tools and resources"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Agent tools and resources"
         
           track-name="agent tools and resources"
         
       >
    Agent tools and resources
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://developer.android.com/studio/preview"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://developer.android.com/studio/preview"
    
       track-type="nav"
       track-metadata-position="nav - android studio preview"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Android Studio preview"
         
           track-name="android studio preview"
         
       >
    Android Studio preview
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://developer.android.com/build/gradle-build-overview"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://developer.android.com/build/gradle-build-overview"
    
       track-type="nav"
       track-metadata-position="nav - gradle build guides"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Gradle build guides"
         
           track-name="gradle build guides"
         
       >
    Gradle build guides
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://developer.android.com/tools"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://developer.android.com/tools"
    
       track-type="nav"
       track-metadata-position="nav - sdk tools guides"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: SDK tools guides"
         
           track-name="sdk tools guides"
         
       >
    SDK tools guides
  
    </a>
    
  
          </tab>
        
      
    </nav>

  </devsite-tabs>

          
          
        </div>
      
    </div>
  </div>

</div>



  

  
</devsite-header>
        <devsite-book-nav scrollbars >
          
            





















<div class="devsite-book-nav-filter"
     >
  <span class="filter-list-icon material-icons" aria-hidden="true"></span>
  <input type="text"
         placeholder="Filter"
         
         aria-label="Type to filter"
         role="searchbox">
  
  <span class="filter-clear-button hidden"
        data-title="Clear filter"
        aria-label="Clear filter"
        role="button"
        tabindex="0"></span>
</div>

<nav class="devsite-book-nav devsite-nav nocontent" data-nosnippet
     aria-label="Side menu">
  <div class="devsite-mobile-header">
    <button type="button"
            id="devsite-close-nav"
            class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
            data-category="Site-Wide Custom Events"
            data-label="Close navigation"
            aria-label="Close navigation">
    </button>
    <div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="androidDevelopers" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/lockup-dark-theme.png"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/lockup.png" class="devsite-site-logo" alt="Android Developers">
  </picture>
  
</a>


</div>
  </div>

  <div class="devsite-book-nav-wrapper">
    <div class="devsite-mobile-nav-top">
      
        <ul class="devsite-nav-list">
          
            <li class="devsite-nav-item">
              
  
  <a href="/get-started"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Essentials"
      
        track-name="essentials"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Essentials"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Essentials
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Essentials"
      
        track-name="essentials"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Essentials">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Essentials">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/design"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Design &amp; Plan"
      
        track-name="design &amp; plan"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Design &amp; Plan"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Design &amp; Plan
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Design &amp; Plan"
      
        track-name="design &amp; plan"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Design &amp; Plan">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Design &amp; Plan">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/develop"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Develop"
      
        track-name="develop"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Develop"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Develop
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Develop"
      
        track-name="develop"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Develop">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Develop">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
                <ul class="devsite-nav-responsive-tabs">
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/studio"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Download"
      
        track-name="download"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Download"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Download
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/studio/intro"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: IDE guides"
      
        track-name="ide guides"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: IDE guides"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip menu="_book">
      IDE guides
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/ai-in-android"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: AI in Android Studio"
      
        track-name="ai in android studio"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI in Android Studio"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      AI in Android Studio
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/tools/agents"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Agent tools and resources"
      
        track-name="agent tools and resources"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Agent tools and resources"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Agent tools and resources
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/studio/preview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Android Studio preview"
      
        track-name="android studio preview"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android Studio preview"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android Studio preview
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/build/gradle-build-overview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Gradle build guides"
      
        track-name="gradle build guides"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Gradle build guides"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Gradle build guides
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/tools"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: SDK tools guides"
      
        track-name="sdk tools guides"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: SDK tools guides"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      SDK tools guides
   </span>
    
  
  </a>
  

  
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/distribute"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Google Play"
      
        track-name="google play"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Play"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Play
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Google Play"
      
        track-name="google play"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Google Play">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Google Play">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/blog"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Blog"
      
        track-name="blog"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Blog"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Blog
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Blog"
      
        track-name="blog"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Blog">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Blog">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
          
    
    
<li class="devsite-nav-item">

  
  <a href="/studio"
    
       class="devsite-nav-title gc-analytics-event "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android Studio"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android Studio
   </span>
    
  
  </a>
  

</li>

  
          
        </ul>
      
    </div>
    
      <div class="devsite-mobile-nav-bottom">
        
          
          <ul class="devsite-nav-list" menu="_book">
            <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>What&#39;s new in Android Studio</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/releases"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Android Studio Rabbit 1 release notes</span></a></li><li class="devsite-nav-item"><a href="/studio/releases/emulator"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Android Emulator release notes</span></a></li><li class="devsite-nav-item"><a href="/studio/releases/past-releases"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Past Android Studio releases</span></a></li><li class="devsite-nav-item"><a href="/studio/releases/studio-release-names"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Android Studio release names</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Service integrations</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/services"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/services/deprecated"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deprecated service integrations</span></a></li></ul></div></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Get started with Android Studio</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/intro"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/install"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Install Android Studio</span></a></li><li class="devsite-nav-item"><a href="/studio/intro/new-ui"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>New UI in Android Studio</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Get to know the UI</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/intro/user-interface"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/intro/accessibility"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Accessibility features</span></a></li><li class="devsite-nav-item"><a href="/studio/intro/keyboard-shortcuts"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Keyboard shortcuts</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/workflow"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Workflow basics</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Manage your project</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/projects"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/projects/create-project"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create a project</span></a></li><li class="devsite-nav-item"><a href="/studio/intro/migrate"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate to Android Studio</span></a></li><li class="devsite-nav-item"><a href="/studio/projects/version-control"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Version control basics</span></a></li><li class="devsite-nav-item"><a href="/studio/intro/studio-config"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure the IDE</span></a></li><li class="devsite-nav-item"><a href="/studio/intro/update"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Update the IDE and tools</span></a></li><li class="devsite-nav-item"><a href="/guide/app-bundle/dynamic-delivery"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>About Play Feature Delivery</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Add C and C++ code</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/projects/add-native-code"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/projects/install-ndk"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Install NDK and CMake</span></a></li><li class="devsite-nav-item"><a href="/studio/projects/configure-agp-ndk"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure the NDK for AGP</span></a></li><li class="devsite-nav-item"><a href="/studio/projects/configure-cmake"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure CMake</span></a></li><li class="devsite-nav-item"><a href="/studio/projects/gradle-external-native-builds"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Link Gradle</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/projects/android-library"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create an Android library</span></a></li><li class="devsite-nav-item"><a href="/studio/projects/continuous-integration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up continuous integration</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Write your code</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/write"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Write your code quicker and more efficiently</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Work with templates</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/projects/templates"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Add code from a template</span></a></li><li class="devsite-nav-item"><a href="/studio/write/sample-code"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Find sample code</span></a></li><li class="devsite-nav-item"><a href="/studio/write/create-java-class"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create a Java class or type</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/projects/add-app-module"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Add a module for a new device</span></a></li><li class="devsite-nav-item"><a href="/studio/write/java8-support"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use Java 8 language features</span></a></li><li class="devsite-nav-item"><a href="/studio/write/java8-support-table"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Java 8 language support table</span></a></li><li class="devsite-nav-item"><a href="/studio/write/add-resources"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Add app resources</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Use tools to develop UI</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/jetpack/compose/tooling/previews"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Develop a layout with Compose ⍈</span></a></li><li class="devsite-nav-item"><a href="/develop/ui/compose/animation/introduction"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create animations with Compose ⍈</span></a></li><li class="devsite-nav-item"><a href="/studio/write/resource-manager"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Manage UI resources</span></a></li><li class="devsite-nav-item"><a href="/studio/write/vector-asset-studio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Add multi-density vector graphics</span></a></li><li class="devsite-nav-item"><a href="/studio/write/create-app-icons"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create app icons</span></a></li><li class="devsite-nav-item"><a href="/studio/write/draw9patch"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create resizable bitmaps (9-patch)</span></a></li><li class="devsite-nav-item"><a href="/studio/write/convert-webp"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create WebP images</span></a></li><li class="devsite-nav-item"><a href="/studio/write/translations-editor"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Localize the UI</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/write/app-link-indexing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Add Android app links</span></a></li><li class="devsite-nav-item"><a href="/studio/write/firebase"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Connect to Firebase</span></a></li><li class="devsite-nav-item"><a href="/studio/write/lint"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Improve your code with lint checks</span></a></li><li class="devsite-nav-item"><a href="/studio/write/annotations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Improve code inspection with annotations</span></a></li><li class="devsite-nav-item"><a href="/studio/write/tool-attributes"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Tools attributes reference</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Run and debug your app</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/run"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Run your app on virtual devices</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/run/managing-avds"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create and manage virtual devices</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Run your app with Android Emulator</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/run/emulator"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/run/resizable-emulator"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Test on multiple screen sizes</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-take-screenshots"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Take screenshots</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-record-screen"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Record the screen</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-use-camera"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use the camera</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-launch-separate-window"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Launch in a separate window</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-launch-without-app"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Launch without running an app</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-install-add-files"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Install and add files</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Use advanced Android Emulator features</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/run/emulator-extended-controls"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use extended controls</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-snapshots"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use snapshots</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-commandline"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use the emulator from the command line</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-console"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Send console commands</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-acceleration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure hardware acceleration</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-comparison"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Emulator feature comparison</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Use emulator networking</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/run/emulator-networking"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-networking-interconnect"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Interconnect emulators</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-networking-address"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Network addresses</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-networking-proxy"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up proxy</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-networking-dns"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up DNS</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-networking-voice"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up voice/SMS</span></a></li><li class="devsite-nav-item"><a href="/studio/run/emulator-networking-advanced"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Advanced networking</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/run/emulator-troubleshooting"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Troubleshoot emulator</span></a></li></ul></div></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/run/android-device-streaming"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Android Device Streaming</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Run your app on a local device</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/run/device"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/studio/run/oem-usb"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Install OEM USB drivers</span></a></li><li class="devsite-nav-item"><a href="/studio/run/win-usb"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get the Google USB driver</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Debug your code</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/debug"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started debugging your code</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/dev-options"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure developer options</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/logcat"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Write and view logs</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Analyze and address crash issues</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/debug/stacktraces"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Analyze a stack trace</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/app-quality-insights"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Analyze Crashlytics and Vitals reports</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/debug/layout-inspector"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Debug your layout</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/universal-problems-panel"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>View design issues</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/network-profiler"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Inspect network traffic</span></a></li><li class="devsite-nav-item"><a href="/studio/inspect/database"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Debug your database</span></a></li><li class="devsite-nav-item"><a href="/studio/inspect/task"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Debug your WorkManager Workers</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/device-file-explorer"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>View on-device files</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/apk-debugger"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Debug pre-built APKs</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/am-screenshot"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Take a screenshot</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/am-video"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Record a video</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/bug-report"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Capture and read bug reports</span></a></li><li class="devsite-nav-item"><a href="/studio/debug/apk-analyzer"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Analyze your APK or AAB</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/run/rundebugconfig"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Customize run/debug configurations</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Test your code</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/test"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Choose a testing method</span></a></li><li class="devsite-nav-item"><a href="/studio/test/test-in-android-studio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Test in Android Studio</span></a></li><li class="devsite-nav-item"><a href="/studio/test/managed-devices"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Test with build-managed devices</span></a></li><li class="devsite-nav-item"><a href="/studio/test/espresso-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Test against screen changes</span></a></li><li class="devsite-nav-item"><a href="/studio/test/command-line"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Test from the command line</span></a></li><li class="devsite-nav-item"><a href="/studio/test/coverage-report"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>View code coverage reports</span></a></li><li class="devsite-nav-item"><a href="/studio/test/on-device-code-coverage"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>View code coverage reports (with on-device agent)</span></a></li><li class="devsite-nav-item"><a href="/studio/test/advanced-test-setup"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up advanced test configurations</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Use specialized testing tools</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/test/other-testing-tools/espresso-test-recorder"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create UI tests</span></a></li><li class="devsite-nav-item"><a href="/studio/test/other-testing-tools/app-crawler"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up automatic testing of your code</span></a></li><li class="devsite-nav-item"><a href="/studio/test/other-testing-tools/monkey"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Stress-test your code with user events</span></a></li><li class="devsite-nav-item"><a href="/studio/preview/backup-restore-testing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Automate backup and restore tests</span></a></li></ul></div></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Inspect performance issues</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/profile"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Record a system trace</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/profile/cpu-profiler"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/inspect-traces"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Inspect traces</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/jank-detection"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Detect UI jank</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/power-profiler"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Inspect power usage</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/generate-trace-logs"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Generate trace logs</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/studio/profile/capture-heap-dump"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Capture a heap dump</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/sample-callstack"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Sample the callstack</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/record-java-kotlin-allocations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Record Java/Kotlin allocations</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/record-java-kotlin-methods"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Record Java/Kotlin methods</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/record-native-allocations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Record native allocations</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/inspect-app-live"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Inspect your app live</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/apk-profiler"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Inspect pre-built APKs</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/standalone-profiler"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Run the standalone profiler</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/build-run-manually"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Build and run a profileable app manually</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Chart glossary</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/profile/chart-glossary/call-chart"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Call chart</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/chart-glossary/events-table"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Events table</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/chart-glossary/flame-chart"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Flame chart</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/chart-glossary/process-memory"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Process memory (RSS)</span></a></li><li class="devsite-nav-item"><a href="/studio/profile/chart-glossary/top-bottom-charts"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Top down and bottom up charts</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-beta"><a href="/android-performance-analyzer"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Android Performance Analyzer (APA)</span><span class="devsite-nav-icon material-icons"
        data-icon="beta"
        data-title="Beta"
        aria-hidden="true"></span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Publish your app</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/studio/publish"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/studio/publish/insights"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Play Policy Insights</span></a></li><li class="devsite-nav-item"><a href="/studio/publish/preparing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Prepare for release</span></a></li><li class="devsite-nav-item"><a href="/studio/publish/versioning"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Version your app</span></a></li><li class="devsite-nav-item"><a href="/studio/publish/app-signing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Sign your app</span></a></li><li class="devsite-nav-item"><a href="/studio/publish/upload-bundle"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Upload your app</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/studio/troubleshoot"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Troubleshoot</span></a></li>

  <li class="devsite-nav-item"><a href="/studio/known-issues"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Known issues</span></a></li>

  <li class="devsite-nav-item"><a href="/studio/report-bugs"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Report a bug</span></a></li>
          </ul>
        
        
          
    
      
      <ul class="devsite-nav-list" menu="Essentials"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Build AI experiences
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/ai"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Get started"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Get started
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Get started
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/get-started/overview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Hello, world!"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Hello, world!
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/adaptive-apps"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Adaptive apps"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Adaptive apps
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/compose"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Compose for UI"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Compose for UI
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/studio"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI-powered IDE"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      AI-powered IDE
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://google.play/business/guides/play-commerce/"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Monetization with Play ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Monetization with Play ↗️
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/developer-verification"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Developer Verification"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Developer Verification
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/registered-app-stores"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Registered App Stores"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Registered App Stores
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Optimize by form factor
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/phones-tablets-foldables"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Phones, tablets, foldables"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Phones, tablets, foldables
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/cars"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android for Cars"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android for Cars
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/tv"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android TV"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android TV
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/xr"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android XR"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android XR
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/googlebook"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Googlebook"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Googlebook
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/chrome-os"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: ChromeOS"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      ChromeOS
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/wear"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Wear OS"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Wear OS
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Build by category
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/games"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Games"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Games
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/media"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Camera &amp; media"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Camera &amp; media
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/social-and-messaging"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Social &amp; messaging"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Social &amp; messaging
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/health-and-fitness"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Health &amp; fitness"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Health &amp; fitness
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/productivity"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Productivity"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Productivity
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/work/overview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Enterprise apps"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Enterprise apps
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Get the latest
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/latest-updates"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Latest updates"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Latest updates
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/latest-updates/experimental"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Experimental updates"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Experimental updates
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/studio/preview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android Studio preview"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android Studio preview
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/jetpack/androidx/versions"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Jetpack &amp; Compose libraries"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Jetpack &amp; Compose libraries
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/training/wearables/versions/latest"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Wear OS releases"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Wear OS releases
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design-for-safety/privacy-sandbox"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Privacy Sandbox ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Privacy Sandbox ↗️
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Design &amp; Plan"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Excellent Experiences
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/quality/excellent"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Learn more"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Learn more
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      UI Design
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Design for Android"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Design for Android
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/mobile"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Mobile"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Mobile
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/desktop"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Desktop experiences"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Desktop experiences
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/xr"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: XR Headsets &amp; XR Glasses"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      XR Headsets &amp; XR Glasses
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/ai-glasses"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI Glasses"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      AI Glasses
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/widget"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Widgets"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Widgets
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/wear"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Wear OS"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Wear OS
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/tv"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android TV"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android TV
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/design/ui/cars"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android for Cars"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android for Cars
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Architecture
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/topic/architecture/intro"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Introduction"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Introduction
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/topic/libraries/view-binding"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Libraries"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Libraries
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/guide/navigation/navigation-principles"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Navigation"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Navigation
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/topic/modularization"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Modularization"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Modularization
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/training/testing/fundamentals"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Testing"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Testing
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/kotlin/multiplatform"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Kotlin Multiplatform"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Kotlin Multiplatform
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Quality
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/quality"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Overview"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Overview
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/quality/core-value"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Core value"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Core value
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/quality/user-experience"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: User experience"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      User experience
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/guide/topics/ui/accessibility"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Accessibility"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Accessibility
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/quality/technical"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Technical quality"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Technical quality
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/quality/excellent"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Excellent Experiences"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Excellent Experiences
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Security
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/security"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Overview"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Overview
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/privacy"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Privacy"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Privacy
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/privacy#app-permissions"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Permissions"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Permissions
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/identity"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Identity"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Identity
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/security/fraud-prevention"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Fraud prevention"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Fraud prevention
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Develop"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Build more with agents in Android
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/ai-in-android"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Learn more"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Learn more
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/cli"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Get Android CLI"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Get Android CLI
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Core areas
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/samples"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Samples"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Samples
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/multidevice"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Multidevice support"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Multidevice support
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/develop/ui"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: User interfaces"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      User interfaces
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/develop/background-work"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Background work"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Background work
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/guide/topics/data"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Data and files"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Data and files
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/develop/connectivity"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Connectivity"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Connectivity
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/develop#core-areas"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: All core areas ⤵️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      All core areas ⤵️
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Tools and workflow
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/studio/write"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Write and debug code"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Write and debug code
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/build/gradle-build-overview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Build projects"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Build projects
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/training/testing"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Test your app"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Test your app
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/topic/performance/overview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Performance"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Performance
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/tools"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Command-line tools"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Command-line tools
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/reference/tools/gradle-api"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Gradle plugin API"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Gradle plugin API
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/bench"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android Bench"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android Bench
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/ai-tools"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Build with agents"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Build with agents
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Device tech
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/phones-tablets-foldables"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Phones, tablets, foldables"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Phones, tablets, foldables
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/googlebook"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Googlebook"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Googlebook
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/chrome-os"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: ChromeOS"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      ChromeOS
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/training/cars"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android for Cars"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android for Cars
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/training/tv"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android TV"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android TV
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/develop/xr"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android XR"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android XR
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/training/wearables"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Wear OS"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Wear OS
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/health-and-fitness/guides"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android Health"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android Health
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/develop/better-together"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Better Together"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Better Together
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/develop#devices"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: All devices ⤵️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      All devices ⤵️
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Libraries
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/reference/packages"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android platform"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android platform
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/jetpack/androidx/explorer"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Jetpack libraries"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Jetpack libraries
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/jetpack/androidx/releases/compose"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Compose libraries"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Compose libraries
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://developers.google.com/android/reference/packages"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Play services ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Play services ↗️
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://play.google.com/sdks"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Play SDK index ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Play SDK index ↗️
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Google Play"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Play Console
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="https://play.google.com/console"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Go to Play Console"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Go to Play Console
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://google.play/business/"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Learn more ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Learn more ↗️
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Fundamentals
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/distribute/play-billing"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Monetization"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Monetization
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/google/play/integrity"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Integrity"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Integrity
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/google/play/vitals"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android vitals"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android vitals
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/distribute/play-policies"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Policies"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Policies
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://google.play/business/programs"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Programs ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Programs ↗️
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Games Dev Center
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/games"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Overview"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Overview
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/guide/playcore/asset-delivery"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Asset Delivery"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Asset Delivery
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/games/pgs/overview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Games Services"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Games Services
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/games/playgames/overview"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Games on PC"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Games on PC
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/games/guidelines"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Level Up guidelines"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Level Up guidelines
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/distribute"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: All Play guides ⤵️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      All Play guides ⤵️
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Libraries
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/guide/playcore/feature-delivery"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Feature Delivery"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Feature Delivery
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/guide/playcore/in-app-updates"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play In-app Updates"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play In-app Updates
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/guide/playcore/in-app-review"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play In-app Reviews"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play In-app Reviews
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/google/play/installreferrer"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Install Referrer"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Install Referrer
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://developers.google.com/android/reference/packages"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Play services ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Play services ↗️
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://play.google.com/sdks"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Play SDK index ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Play SDK index ↗️
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/distribute"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: All Play libraries ⤵️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      All Play libraries ⤵️
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Tools &amp; resources
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/guide/app-bundle"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Android App Bundles"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Android App Bundles
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/distribute/marketing-tools"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Brand &amp; marketing"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Brand &amp; marketing
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="https://developers.google.com/android-publisher/api-ref/rest"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Play Console APIs ↗️"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Play Console APIs ↗️
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Blog"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      the Android Developer&#39;s Blog
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/blog/latest"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Read the latest"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Read the latest
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/blog/authors"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Explore the authors →"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Explore the authors →
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Explore categories
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/blog/categories/product-news"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Product News"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Product News
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/blog/categories/community"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Community"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Community
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/blog/categories/how-tos"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: How-tos"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      How-tos
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/blog/categories/case-studies"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Case Studies"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Case Studies
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/blog/categories/events-and-programs"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Events &amp; Programs"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Events &amp; Programs
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/blog/categories/documentation"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Documentation"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Documentation
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
        
        
          
    
  
    
  
    
  
    
  
    
  
    
  
    
  
        
      </div>
    
  </div>
</nav>
          
        </devsite-book-nav>
      
      <section id="gc-wrapper">
        <main role="main" id="main-content" class="devsite-main-content"
            
              has-book-nav
              has-sidebar
            >
          <div class="devsite-sidebar">
            <div class="devsite-sidebar-content">
                
                <devsite-toc class="devsite-nav"
                            role="navigation"
                            aria-label="On this page"
                            depth="2"
                            scrollbars
                            data-nosnippet
                  ></devsite-toc>
                <devsite-recommendations-sidebar class="nocontent devsite-nav" data-nosnippet>
                </devsite-recommendations-sidebar>
            </div>
          </div>
          <devsite-content>
            
              










<article class="devsite-article">
  
  
  
  
  

  <div class="devsite-article-meta nocontent" role="navigation" data-nosnippet>
    
    
    <ul class="devsite-breadcrumb-list"
  
    aria-label="Breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://developer.android.com/"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Android Developers"
      
    >
    
          Android Developers
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://developer.android.com/develop"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail=""
      
    >
    
          Develop
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://developer.android.com/studio"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="3"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="3"
      
        track-metadata-eventdetail="Android Studio"
      
    >
    
          Android Studio
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://developer.android.com/studio/intro"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="4"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="4"
      
        track-metadata-eventdetail=""
      
    >
    
          IDE guides
        
  </a>
  
      
    
  </li>
  
</ul>
    
      
    <devsite-thumb-rating position="header">
    </devsite-thumb-rating>
  
    
  </div>
  
    <h1 class="devsite-page-title" tabindex="-1">
      Meet Android Studio<devsite-actions hidden data-nosnippet><devsite-feature-tooltip
      ack-key="AckCollectionsBookmarkTooltipDismiss"
      analytics-category="Site-Wide Custom Events"
      analytics-action-show="Callout Profile displayed"
      analytics-action-close="Callout Profile dismissed"
      analytics-label="Create Collection Callout"
      class="devsite-page-bookmark-tooltip nocontent"
      data-nosnippet
      dismiss-button="true"
      id="devsite-collections-dropdown"
      
      dismiss-button-text="Dismiss"

      
      close-button-text="Got it">

    
    
      <devsite-bookmark></devsite-bookmark>
    

    <span slot="popout-heading">
      
      Stay organized with collections
    </span>
    <span slot="popout-contents">
      
      Save and categorize content based on your preferences.
    </span>
  </devsite-feature-tooltip>
    <devsite-llm-tools></devsite-llm-tools></devsite-actions>
  
      
    </h1>
  <div class="devsite-page-title-meta"><devsite-view-release-notes></devsite-view-release-notes></div>
  

  <devsite-toc class="devsite-nav"
    depth="2"
    devsite-toc-embedded
    >
  </devsite-toc>
  
    
    <devsite-recommendations-dropdown class="nocontent" data-nosnippet>
    </devsite-recommendations-dropdown>
    
  <div class="devsite-article-body clearfix
  ">

  
    
    























































































































 





























 











 











 





<p>Android Studio is the official Integrated Development Environment (IDE) for
Android app development. Based on the powerful code editor and developer tools
from <a href="https://www.jetbrains.com/idea/" class="external">IntelliJ IDEA</a>, Android
Studio offers even more features that enhance your productivity when building
Android apps, such as:</p>

<ul>
<li>A flexible Gradle-based build system</li>
<li>A fast and feature-rich emulator</li>
<li>A unified environment where you can develop for all Android devices</li>
<li>Live Edit to update composables in emulators and physical devices in real
time</li>
<li>Code templates and GitHub integration to help you build common app features
and import sample code</li>
<li>Extensive testing tools and frameworks</li>
<li>Lint tools to catch performance, usability, version compatibility, and other
problems</li>
<li>C++ and NDK support</li>
</ul>

<p>This page provides an introduction to basic Android Studio features.
For a summary of the latest changes, see the
<a href="/studio/releases">Android Studio release notes</a>.</p>

<h2 id="project-structure" data-text="Project structure" tabindex="-1">Project structure</h2>

<div class="attempt-right" style="width:398px">
<img alt src="/static/studio/images/project-android-view.png">
<p class="img-caption"><strong>Figure 1.</strong> Project files in
  <b>Android</b> view.</p>
</div>

<p>Each project in Android Studio contains one or more modules with source code
files and resource files. The types of modules include:</p>

<ul>
<li>Android app modules</li>
<li>Library modules</li>
<li>Google App Engine modules</li>
</ul>

<p>By default, Android Studio displays your project files in the <strong>Android</strong> view,
as shown in figure 1. This view is organized by modules to provide quick
access to your project&#39;s key source files. All the build files are visible at
the top level, under <strong>Gradle Scripts</strong>.</p>

<p>Each app module contains the following folders:</p>

<ul>
<li><strong>manifests</strong>: Contains the <code translate="no" dir="ltr">AndroidManifest.xml</code> file.</li>
<li><strong>kotlin+java</strong>: Contains the Kotlin and Java source code files, including
JUnit test code.</li>
<li><strong>res</strong>: Contains all non-code resources such as UI strings and images.</li>
</ul>

<p>The Android project structure on disk differs from this flattened
representation. To see the actual file structure of the project, select
<strong>Project</strong> instead of <strong>Android</strong> from the <strong>Project</strong> menu.</p>

<p>For more information, see <a href="/studio/projects">Projects overview</a>.</p>

<h2 id="build-system" data-text="Gradle build system" tabindex="-1">Gradle build system</h2>

<p>Android Studio uses Gradle as the foundation of the build system, with more
Android-specific capabilities provided by the
<a href="/build/releases/gradle-plugin">Android Gradle plugin</a>. This build
system runs as an integrated tool from the Android Studio menu and
independently from the command line. You can use the features of the build
system to do the following:</p>

<ul>
<li>Customize, configure, and extend the build process.</li>
<li>Create multiple APKs for your app with different features, using the same
project and modules.</li>
<li>Reuse code and resources across source sets.</li>
</ul>

<p>By employing the flexibility of Gradle, you can achieve all of this without
modifying your app&#39;s core source files.</p>

<p>Android Studio build files are named <code translate="no" dir="ltr">build.gradle.kts</code> if you use
<a href="https://kotlinlang.org" class="external">Kotlin</a> (recommended) or <code translate="no" dir="ltr">build.gradle</code> if
you use <a href="http://groovy-lang.org" class="external">Groovy</a>. They are plain text files
that use the Kotlin or Groovy syntax to configure the build with elements
provided by the Android Gradle plugin. Each project has one top-level build file
for the entire project and separate module-level build files for each module.
When you import an existing project, Android Studio automatically generates the
necessary build files.</p>
<aside class="note"><strong>Note:</strong><span> We might reference either the <code translate="no" dir="ltr">build.gradle.kts</code> or <code translate="no" dir="ltr">build.gradle</code>
file alone in the documentation, but they&#39;re conceptually interchangeable. For
example if you see <code translate="no" dir="ltr">build.gradle.kts</code> but you use the Groovy DSL to configure
your build, you can think of it as the <code translate="no" dir="ltr">build.gradle</code> file (and the other way
around).</span></aside>
<p>To learn more about the build system and how to configure your build, see
<a href="/build">Configure your build</a>.</p>

<h3 id="build-variants" data-text="Build variants" tabindex="-1">Build variants</h3>

<p>The build system can help you create different versions of the same app
from a single project. This is useful when you have both a free version and a
paid version of your app or if you want to distribute multiple APKs for
different device configurations on Google Play.</p>

<p>For more information about configuring build variants, see
<a href="/build/build-variants">Configure build variants</a>.</p>

<h3 id="resource-shrinking" data-text="Resource shrinking" tabindex="-1">Resource shrinking</h3>

<p>Resource shrinking in Android Studio automatically removes unused resources
from your packaged app and library dependencies. For example, if you add an
image or string to your project but never actually reference it in your UI,
resource shrinking safely removes that asset from your packaged app.</p>
<aside class="note"><strong>Note:</strong><span> Resource shrinking works in conjunction
with code shrinking tools, such as R8.</span></aside>
<p>For more information on shrinking code and resources, see
<a href="/topic/performance/app-optimization/enable-app-optimization">Enable app optimization with R8</a>.</p>

<h3 id="dependencies" data-text="Manage dependencies" tabindex="-1">Manage dependencies</h3>

<p>Dependencies for your project are specified by name in the module-level build
script. Gradle finds dependencies and makes them available in your build. You
can declare module dependencies, remote binary dependencies, and local binary
dependencies in your <code translate="no" dir="ltr">build.gradle.kts</code> file.</p>

<p>Android Studio configures projects to use the Maven Central Repository by
default. This configuration is included in the top-level build file for the
project.</p>

<p>For more information about configuring dependencies, read
<a href="/build/dependencies">Add build dependencies</a>.</p>

<h2 id="debug-perf" data-text="Debug and profile tools" tabindex="-1">Debug and profile tools</h2>

<p>Android Studio helps you debug and improve the performance of your
code, including inline debugging and performance analysis tools.</p>

<h3 id="inline-debug" data-text="Inline debugging" tabindex="-1">Inline debugging</h3>

<p>Use inline debugging to enhance your code walkthroughs in the debugger view
with inline verification of references, expressions, and variable values.</p>

<p>Inline debug information includes:</p>

<ul>
<li>Inline variable values</li>
<li>Objects that reference a selected object</li>
<li>Method return values</li>
<li>Lambda and operator expressions</li>
<li>Tooltip values</li>
</ul>

<p>To enable inline debugging, in the <strong>Debug</strong> window, click <strong>Settings</strong>
<img src="/static/studio/images/studio-debug-settings-icon.png" class="inline-icon"
alt=""/> and select <strong>Show Variable Values in Editor</strong>.</p>

<h3 id="layout-inspector" data-text="Layout Inspector" tabindex="-1">Layout Inspector</h3>

<p>Layout Inspector lets you inspect a Compose layout inside a running app in an
emulator or physical device. You can use the Layout Inspector to check how
often a composable is recomposed or skipped, which can help identify issues
with your app.</p>

<p>To start the Layout Inspector, <a href="/studio/run">run your app</a>, go to the
<strong>Running Devices</strong> window, and click <strong>Toggle Layout Inspector</strong>
<img src="/static/studio/images/design/start-embedded-layout-inspector.png" class="inline-icon" alt>.
If you switch among multiple devices or projects, the Layout Inspector
automatically connects to the debuggable processes running in the foreground of
the connected device.</p>

<p>For more information, see <a href="/studio/debug/layout-inspector">Layout Inspector</a>.</p>

<h3 id="monitors" data-text="Performance profilers" tabindex="-1">Performance profilers</h3>

<p>Android Studio provides performance profilers so you can easily track your
app&#39;s memory and CPU usage, find deallocated objects, locate memory leaks,
optimize graphics performance, and analyze network requests.</p>

<p>To use performance profilers, with your app running on a device or emulator,
open the Android Profiler by selecting <strong>View &gt; Tool Windows &gt; Profiler</strong>.</p>

<p>For more information about performance profilers, see
<a href="/studio/profile">Profile your app performance</a>.</p>

<h3 id="heap-dump" data-text="Heap dump" tabindex="-1">Heap dump</h3>

<p>When profiling memory usage in Android Studio, you can simultaneously
initiate garbage collection and dump the Java heap to a heap snapshot in an
Android-specific <code translate="no" dir="ltr">HPROF</code> binary format file. The HPROF viewer displays classes,
instances of each class, and a reference tree to help you track memory usage
and find memory leaks.</p>

<p>For more information about working with heap dumps, see
<a href="/studio/profile/capture-heap-dump">Capture a heap dump</a>.</p>

<h3 id="allocation" data-text="Memory Profiler" tabindex="-1">Memory Profiler</h3>

<p>Use Memory Profiler to track memory allocation and watch where objects
are being allocated when you perform certain actions. These allocations help you
optimize your app&#39;s performance and memory use by adjusting the
method calls related to those actions.</p>

<p>For information about tracking and analyzing allocations, see
<a href="/studio/profile/capture-heap-dump#heap-dump-overview">Heap dump overview</a>.</p>

<h3 id="data-file" data-text="Data file access" tabindex="-1">Data file access</h3>

<p>The Android SDK tools, such as <a href="/topic/performance/tracing/command-line">Systrace</a> and <a href="/studio/debug/am-logcat">Logcat</a>,
generate performance and debugging data for detailed app analysis.</p>

<p>To view the available generated data files:</p>

<ol>
<li>Open the Android Profile and select Past Recordings.</li>
<li>In the list of the generated files, double-click a file to view the data.</li>
<li>Right-click any HPROF files to convert them to the standard.</li>
<li>Investigate your RAM usage file format.</li>
</ol>

<h3 id="code-inspection" data-text="Code inspections" tabindex="-1">Code inspections</h3>

<p>Whenever you compile your program, Android Studio automatically runs configured
<a href="/studio/write/lint">lint</a> checks and other <a href="https://www.jetbrains.com/help/idea/2026.1/code-inspection.html" class="external">IDE inspections</a> to help you easily
identify and correct problems with the structural quality of your code.</p>

<p>The lint tool checks your Android project source files for potential bugs and
optimization improvements for correctness, security, performance, usability,
accessibility, and internationalization.</p>

<p><img src="/static/studio/images/lint-inspection-results.png"
alt="" id="lint-inspection"/></p>

<p class="img-caption">
  <strong>Figure 2.</strong> The results of a lint inspection in Android Studio.
</p>

<p>In addition to lint checks, Android Studio performs IntelliJ code
inspections and validates annotations to streamline your coding workflow.</p>

<p>For more information, see
<a href="/studio/write/lint">Improve your code with lint checks</a>.</p>

<h3 id="annotations" data-text="Annotations in Android Studio" tabindex="-1">Annotations in Android Studio</h3>

<p>Android Studio supports annotations for variables, parameters, and return
values to help you catch bugs, such as null pointer exceptions and resource
type conflicts.</p>

<p>The Android SDK Manager packages the Jetpack Annotations
library in the Android Support Repository for use with Android Studio. Android
Studio validates the configured annotations during code inspection.</p>

<p>For more details about Android annotations, see
<a href="/studio/write/annotations">Improve code inspection with annotations</a>.</p>

<h3 id="log-message" data-text="Log messages" tabindex="-1">Log messages</h3>

<p>When you build and run your app with Android Studio, you can view
<a href="/studio/command-line/adb"><code translate="no" dir="ltr">adb</code></a> output and device log messages
in the <a href="/studio/debug/am-logcat"><strong>Logcat</strong> window</a>.</p>

<h2 id="sign-in" data-text="Sign in to your developer account" tabindex="-1">Sign in to your developer account</h2>

<p>Sign in to your developer account in Android Studio to access
additional tools that require authentication, such as Firebase and Android
Vitals in <a href="/studio/debug/app-quality-insights">App Quality Insights</a> and
<a href="/studio/preview/gemini">Gemini in Android Studio</a>. By signing in, you give
those tools permission to view and manage your data across Google services.</p>

<p>To sign in to your developer account in Android Studio, click the profile icon
<img src="/static/studio/images/intro/profile-icon.png" alt class="inline-icon"> at
the end of the toolbar. Follow the prompts to provide the IDE with only the
permissions required for each feature you want to enable. If you&#39;re already
signed in, manage the permissions at <strong>File</strong> (<strong>Android Studio</strong> on macOS) &gt;
<strong>Settings</strong> &gt; <strong>Tools</strong> &gt; <strong>Google Accounts</strong>.</p>

  

  
    <devsite-hats-survey class="nocontent" data-nosnippet
      hats-id="VxqvKSur40kxBYCLVTd0SSGykbno"
      listnr-id="5207477"></devsite-hats-survey>
  
</div>

  
    
      <devsite-recommendations display="in-page" hidden yield>
      </devsite-recommendations>
    
    
      
    <devsite-thumb-rating position="footer">
    </devsite-thumb-rating>
  
       
    
    
      <devsite-recommendations id="recommendations-link" yield></devsite-recommendations>
    
  

  <div class="devsite-floating-action-buttons"></div></article>


<devsite-content-footer class="nocontent" data-nosnippet>
  <p>Content and code samples on this page are subject to the licenses described in the <a href="/license">Content License</a>. Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.</p>
  <p>Last updated 2026-10-16 UTC.</p>
</devsite-content-footer>


<devsite-notification
>
</devsite-notification>


  
<div class="devsite-content-data">
  
  
    <template class="devsite-content-data-template">
      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]]
    </template>
  
</div>
            
          </devsite-content>
        </main>
        <devsite-footer-promos class="devsite-footer">
          
            

<nav class="devsite-footer-promos nocontent"
     aria-label="Promotions"
     data-nosnippet>
  <ul class="devsite-footer-promos-list">
    
    <li class="devsite-footer-promo">
      <a href="//x.com/AndroidDev"
         class="devsite-footer-promo-title gc-analytics-event"
         data-category="Site-Wide Custom Events"
       
       
         data-label="Footer X Promo"
       >
        
        
        <picture>
          
          <source class="devsite-dark-theme"
                  srcset="https://developer.android.com/_static/android/images/logo-x_dt.svg"
                  media="(prefers-color-scheme: dark)">
          
          <img class="devsite-footer-promo-icon"
                src="/_static/android/images/logo-x.svg"
                loading="lazy"
                alt="X">
        </picture>
        
        <span class="devsite-footer-promo-label">
          X
        </span>
      </a>
      <div class="devsite-footer-promo-description">Follow @AndroidDev on X</div>
    </li>
    
    <li class="devsite-footer-promo">
      <a href="//www.youtube.com/user/androiddevelopers"
         class="devsite-footer-promo-title gc-analytics-event"
         data-category="Site-Wide Custom Events"
       
       
         data-label="Footer YouTube Promo"
       >
        
        
        <picture>
          
          <source class="devsite-dark-theme"
                  srcset="https://developer.android.com/_static/android/images/logo-youtube_dt.svg"
                  media="(prefers-color-scheme: dark)">
          
          <img class="devsite-footer-promo-icon"
                src="//www.gstatic.com/images/icons/material/product/2x/youtube_48dp.png"
                loading="lazy"
                alt="YouTube">
        </picture>
        
        <span class="devsite-footer-promo-label">
          YouTube
        </span>
      </a>
      <div class="devsite-footer-promo-description">Check out Android Developers on YouTube</div>
    </li>
    
    <li class="devsite-footer-promo">
      <a href="//www.linkedin.com/showcase/androiddev"
         class="devsite-footer-promo-title gc-analytics-event"
         data-category="Site-Wide Custom Events"
       
       
         data-label="Footer LinkedIn Promo"
       >
        
        
        <picture>
          
          <source class="devsite-dark-theme"
                  srcset="https://developer.android.com/_static/android/images/logo-linkedin_dt.svg"
                  media="(prefers-color-scheme: dark)">
          
          <img class="devsite-footer-promo-icon"
                src="/_static/android/images/logo-linkedin.svg"
                loading="lazy"
                alt="LinkedIn">
        </picture>
        
        <span class="devsite-footer-promo-label">
          LinkedIn
        </span>
      </a>
      <div class="devsite-footer-promo-description">Connect with the Android Developers community on LinkedIn</div>
    </li>
    
  </ul>
</nav>

          
        </devsite-footer-promos>
        <devsite-footer-linkboxes class="devsite-footer">
          
            
<nav class="devsite-footer-linkboxes nocontent"
     aria-label="Footer links"
     data-nosnippet>
  
  <ul class="devsite-footer-linkboxes-list">
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">More Android</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.android.com"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Android
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.android.com/enterprise/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Android for Enterprise
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.android.com/security-center/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            Security
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//source.android.com"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Source
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/news"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
          
            News
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//android-developers.googleblog.com/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 6)"
            >
            
          
            Blog
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/podcasts"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 7)"
            >
            
              
              
            
          
            Podcasts
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Discover</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/games"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Gaming
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/ml"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Machine Learning
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/health-and-fitness"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            Health & Fitness
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/media"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Camera & Media
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/privacy"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
          
            Privacy
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/training/connectivity/5g"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 6)"
            >
            
              
              
            
          
            5G
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Android Devices</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/large-screens"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Large screens
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/wear"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Wear OS
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/chrome-os"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            ChromeOS devices
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/cars"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Android for cars
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/tv"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
              
              
            
          
            Android TV
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Releases</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/about/versions/17"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Android 17
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/about/versions/16"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Android 16
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/about/versions/15"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            Android 15
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/about/versions/14"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Android 14
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/about/versions/13"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
          
            Android 13
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/about/versions/12"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 6)"
            >
            
          
            Android 12
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/about/versions/11"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 7)"
            >
            
              
              
            
          
            Android 11
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Documentation and Downloads</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/studio/intro"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Android Studio guide
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/guide"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Developers guides
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/reference"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            API reference
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/studio"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Download Studio
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/ndk"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
              
              
            
          
            Android NDK
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Support</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//issuetracker.google.com/issues/new?component=190923&amp;template=841312"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Report platform bug
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//issuetracker.google.com/issues/new?component=192697"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Report documentation bug
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//support.google.com/googleplay/android-developer"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            Google Play support
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="https://g.co/userresearch/androiddeveloperfooter"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
              
              
            
          
            Join research studies
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
  </ul>
  
</nav>
          
        </devsite-footer-linkboxes>
        <devsite-footer-utility class="devsite-footer">
          
            

<div class="devsite-footer-utility nocontent" data-nosnippet>
  
  
  <nav class="devsite-footer-sites" aria-label="Other Google Developers websites">
    <a href="https://developers.google.com/"
       class="devsite-footer-sites-logo-link gc-analytics-event"
       data-category="Site-Wide Custom Events"
       data-label="Footer Google Developers Link">
      <picture>
        
        <source srcset="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/lockup-google-for-developers-dark-theme.svg"
                media="(prefers-color-scheme: none)"
                class="devsite-dark-theme">
        
        <img class="devsite-footer-sites-logo"
             src="https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/lockup-google-for-developers.svg"
             loading="lazy"
             alt="Google Developers">
      </picture>
    </a>
    <ul class="devsite-footer-sites-list">
      
      <li class="devsite-footer-sites-item">
        <a href="//developer.android.com"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Android Link"
         
         >
          Android
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//developer.chrome.com/home"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Chrome Link"
         
         >
          Chrome
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//firebase.google.com"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Firebase Link"
         
         >
          Firebase
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//cloud.google.com"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Google Cloud Platform Link"
         
         >
          Google Cloud Platform
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//developers.google.com/products/"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer All products Link"
         
         >
          All products
        </a>
      </li>
      
    </ul>
  </nav>
  

  
  <nav class="devsite-footer-utility-links" aria-label="Utility links">
    
    <ul class="devsite-footer-utility-list">
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/privacy"
           data-category="Site-Wide Custom Events"
           data-label="Footer Privacy link"
         >
          Privacy
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="/license"
           data-category="Site-Wide Custom Events"
           data-label="Footer License link"
         >
          License
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="/distribute/marketing-tools/brand-guidelines"
           data-category="Site-Wide Custom Events"
           data-label="Footer Brand guidelines link"
         >
          Brand guidelines
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 glue-cookie-notification-bar-control">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="#"
           data-category="Site-Wide Custom Events"
           data-label="Footer Manage cookies link"
         
           aria-hidden="true"
         >
          Manage cookies
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-utility-button">
        
        <span class="devsite-footer-utility-description">Get news and tips by email</span>
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="/updates"
           data-category="Site-Wide Custom Events"
           data-label="Footer Subscribe link"
         >
          Subscribe
        </a>
        
      </li>
      
    </ul>
    
    
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="id"
        >Indonesia</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="it"
        >Italiano</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pl"
        >Polski</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="vi"
        >Tiếng Việt</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="tr"
        >Türkçe</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ru"
        >Русский</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ar"
        >العربيّة</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fa"
        >فارسی</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="hi"
        >हिंदी</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="bn"
        >বাংলা</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="th"
        >ภาษาไทย</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_tw"
        >中文 – 繁體</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>

  </nav>
</div>
          
        </devsite-footer-utility>
        <devsite-panel>
          
        </devsite-panel>
        
      </section>
      </section>
    <devsite-sitemask></devsite-sitemask>
    <devsite-snackbar></devsite-snackbar>
    <devsite-tooltip ></devsite-tooltip>
    <devsite-heading-link></devsite-heading-link>
    <devsite-analytics>
      
        <script type="application/json" analytics>[]</script>
<script type="application/json" tag-management>{&#34;at&#34;: &#34;True&#34;, &#34;ga4&#34;: [{&#34;id&#34;: &#34;G-QFRN08RN6E&#34;, &#34;purpose&#34;: 0}], &#34;ga4p&#34;: [{&#34;id&#34;: &#34;G-QFRN08RN6E&#34;, &#34;purpose&#34;: 0}], &#34;gtm&#34;: [{&#34;id&#34;: &#34;GTM-KMSWPCJ&#34;, &#34;purpose&#34;: 0}], &#34;parameters&#34;: {&#34;internalUser&#34;: &#34;False&#34;, &#34;language&#34;: {&#34;machineTranslated&#34;: &#34;False&#34;, &#34;requested&#34;: &#34;en&#34;, &#34;served&#34;: &#34;en&#34;}, &#34;pageType&#34;: &#34;article&#34;, &#34;projectName&#34;: &#34;Android Studio&#34;, &#34;signedIn&#34;: &#34;False&#34;, &#34;tenant&#34;: &#34;android&#34;, &#34;recommendations&#34;: {&#34;sourcePage&#34;: &#34;&#34;, &#34;sourceType&#34;: 0, &#34;sourceRank&#34;: 0, &#34;sourceIdenticalDescriptions&#34;: 0, &#34;sourceTitleWords&#34;: 0, &#34;sourceDescriptionWords&#34;: 0, &#34;experiment&#34;: &#34;&#34;}, &#34;experiment&#34;: {&#34;ids&#34;: &#34;&#34;}}}</script>
      
    </devsite-analytics>
    
      <devsite-badger></devsite-badger>
    
    
    
    
<android-fully-clickable
    target="
        .android-case-study .devsite-landing-row-item,
        .android-editorial-and-updates-cards .devsite-card-content-wrapper,
        .android-editorial-and-updates-cards .devsite-landing-row-item,
        .android-grouped-resources .devsite-landing-row-item,
        .android-grouped-resources-contained--primary .devsite-landing-row-item,
        .android-grouped-resources-contained--secondary .devsite-landing-row-item,
        .android-grouped-resources-contained--tertiary .devsite-landing-row-item,
        .android-grouped-resources-uncontained--primary .devsite-landing-row-item,
        .android-grouped-resources-uncontained--secondary .devsite-landing-row-item,
        .android-grouped-resources-uncontained--tertiary .devsite-landing-row-item,
        .android-guide-cards .devsite-landing-row-item,
        .android-illustrated-resources-index .devsite-landing-row-item,
        .android-illustrated-resources-primary .devsite-landing-row-item,
        .android-illustrated-resources-secondary .devsite-landing-row-item,
        .android-illustrated-resources-secondary-small .devsite-landing-row-item,
        .android-illustrated-resources-tertiary .devsite-landing-row-item,
        .android-illustrated-resources-tertiary-small .devsite-landing-row-item,
        .android-promo .devsite-landing-row-item,
        .android-quick-link,
        .android-samples .devsite-card-wrapper,
        .fully-clickable"
    watch=".android-editorial-and-updates-cards, .android-samples, devsite-content"></android-fully-clickable>
    
<script nonce="r8D2+gOrxwbkqoJD/+cLURYUmyuV3M">
  
  (function(d,e,v,s,i,t,E){d['GoogleDevelopersObject']=i;
    t=e.createElement(v);t.async=1;t.src=s;E=e.getElementsByTagName(v)[0];
    E.parentNode.insertBefore(t,E);})(window, document, 'script',
    'https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/js/app_loader.js', '[3,"en",null,"/js/devsite_app_module.js","https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43","https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android","https://android-dot-devsite-v2-prod.appspot.com",1,null,["/_pwa/android/manifest.json","https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/images/video-placeholder.svg","https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/favicon.svg","https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/android/images/lockup.png","https://fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Text:400,400italic,500,500italic,600,600italic,700,700italic|Roboto+Mono:400,500,700&display=swap"],1,null,[1,6,8,12,14,17,21,25,50,52,63,70,75,76,80,87,91,92,93,97,98,100,101,102,103,104,105,107,108,109,110,112,113,116,117,118,120,122,124,125,126,127,129,130,131,132,133,134,135,136,138,140,141,147,148,149,151,152,156,157,158,159,161,163,164,168,169,170,179,180,182,183,186,191,193,196],"AIzaSyAP-jjEJBzmIyKR4F-3XITp8yM9T1gEEI8","AIzaSyB6xiKGDR5O3Ak2okS4rLkauxGUG7XP0hg","developer.android.com","AIzaSyAQk0fBONSGUqCNznf6Krs82Ap1-NV6J4o","AIzaSyCCxcqdrZ_7QMeLCRY20bh_SXdAYqy70KY",null,null,null,["Profiles__enable_complete_playlist_endpoint","MiscFeatureFlags__enable_llms_txt","DevPro__enable_free_benefits","Search__enable_ai_search_summaries_for_all","MiscFeatureFlags__enable_firebase_utm","DevPro__enable_nvidia_credits_card","Profiles__enable_release_notes_notifications","DevPro__enable_enterprise","MiscFeatureFlags__remove_cross_domain_tracking_params","DevPro__enable_google_payments","Concierge__enable_remove_info_panel_tags","Cloud__fast_free_trial","Search__enable_page_map","Search__enable_dynamic_content_confidential_banner","MiscFeatureFlags__developers_footer_dark_image","MiscFeatureFlags__enable_variable_operator","Profiles__enable_join_program_group_endpoint","Cloud__enable_cloud_shell_fte_user_flow","MiscFeatureFlags__enable_variable_operator_index_yaml","DevPro__enable_devsite_captcha","MiscFeatureFlags__developers_footer_image","MiscFeatureFlags__enable_dark_theme","DevPro__enable_credits_banner","Concierge__enable_actions_menu","MiscFeatureFlags__fix_lower_breadcrumbs","TpcFeatures__proxy_prod_host","DevPro__remove_eu_tax_intake_form","Profiles__require_profile_eligibility_for_signin","Concierge__enable_pushui","MiscFeatureFlags__enable_appearance_cookies","CloudShell__cloud_shell_button","Profiles__enable_developer_profile_pages_as_content","Cloud__enable_cloud_shell","DevPro__enable_google_one_card","MiscFeatureFlags__enable_explicit_template_dependencies","Profiles__enable_completecodelab_endpoint","Cloud__enable_cloudx_experiment_ids","Search__enable_ai_eligibility_checks","DevPro__enable_firebase_workspaces_card","DevPro__enable_g1_integration","Analytics__enable_devpro_interaction_logging","DevPro__enable_embed_profile_creation","Cloud__enable_cloud_dlp_service","BookNav__enable_tenant_cache_key","Search__enable_suggestions_from_borg","Profiles__enable_completequiz_endpoint","Profiles__enable_stripe_subscription_management","Cloud__enable_legacy_calculator_redirect","Profiles__enable_callout_notifications","Profiles__enable_page_saving","Profiles__enable_playlist_community_acl","MiscFeatureFlags__enable_framebox_badge_methods","Profiles__enable_developer_profile_benefits_ui_redesign","DevPro__enable_g1_ineligible_redirect","SignIn__enable_l1_signup_flow","MiscFeatureFlags__enable_project_variables","Concierge__enable_devsite_llm_tools","CloudShell__cloud_code_overflow_menu","Search__enable_ai_search_summaries","MiscFeatureFlags__enable_explain_this_code","Cloud__enable_free_trial_server_call","EngEduTelemetry__enable_engedu_telemetry","Profiles__enable_profile_collections","DevPro__enable_developer_subscriptions","DevPro__enable_devpro_offers","Profiles__enable_purchase_prompts","Profiles__enable_recognition_badges","AIStudioInteractionsToggle__interactions_are_default","Analytics__enable_clearcut_logging","DevPro__enable_vertex_credit_card","Profiles__enable_developer_profiles_callout","DevPro__enable_code_assist","Significatio__enable_by_tenant","Profiles__enable_auto_apply_credits","Profiles__enable_targeted_hero","DevPro__enable_google_payments_buyflow","MiscFeatureFlags__enable_view_transitions","DevPro__enable_cloud_innovators_plus","Profiles__enable_dashboard_curated_recommendations","Profiles__enable_public_developer_profiles","Cloud__cache_serialized_dynamic_content","Profiles__enable_awarding_url","MiscFeatureFlags__gdp_dashboard_reskin_enabled","TpcFeatures__enable_unmirrored_page_left_nav","Experiments__reqs_query_experiments","Profiles__enable_user_type"],null,null,"AIzaSyBLEMok-5suZ67qRPzx0qUtbnLmyT_kCVE","https://developerscontentserving-pa.googleapis.com","AIzaSyCM4QpTRSqP5qI4Dvjt4OAScIN8sOUlO-k","https://developerscontentsearch-pa.googleapis.com",2,4,null,"https://developerprofiles-pa.googleapis.com",[3,"android","Android Developers","developer.android.com",null,"android-dot-devsite-v2-prod.appspot.com",null,null,[null,1,null,null,null,null,null,null,null,null,null,[1],null,null,null,null,null,null,[1],[1,null,null,[1,20],"/recommendations"],null,null,null,[1,null,1],[1,1,null,1,1],null,null,null,null,[1],[1]],null,[18,null,null,null,null,null,"/images/lockup.png","/images/touchicon-180.png",null,null,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,"/images/lockup-dark-theme.png",[]],[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[6,1,14,15,20,22,23,28,29,37,43],null,[[],[1,1]],[[null,null,null,null,null,null,null,[["G-QFRN08RN6E"],null,null,[["G-QFRN08RN6E",1]]],null,null,null,null,1],null,[[1,1],[2,2]]],null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,"android.devsite.google"],null,"pk_live_5170syrHvgGVmSx9sBrnWtA5luvk9BwnVcvIi7HizpwauFG96WedXsuXh790rtij9AmGllqPtMLfhe2RSwD6Pn38V00uBCydV4m",1,1,"https://developerscontentinsights-pa.googleapis.com","AIzaSyCg-ZUslalsEbXMfIo9ZP8qufZgo3LSBDU","AIzaSyDxT0vkxnY_KeINtA4LSePJO-4MAZPMRsE","https://developers.googleapis.com",null,null,"AIzaSyBQom12tzI-rybN7Sf-KfeL4nwm-Rf7PmI\n",null,null,"https://developers.googleapis.com"]')
  
</script>

    <devsite-a11y-announce></devsite-a11y-announce>
  </body>
</html>