walker summarize_paragraph{
    has paragraph;
    has url;
    can cl_summer.summarize;

    summary= cl_summer.summarize(text=paragraph,sent_count=2,url=url,summarize_type="LsaSummarizer");
    report summary;
}

walker generate_image{
    has text;
    can text_to_image.generate;

    image=text_to_image.generate(text=text);
    report image;

}