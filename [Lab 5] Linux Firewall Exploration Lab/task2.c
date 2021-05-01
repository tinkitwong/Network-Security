/**
* This code uses Netfilter to implement 5 rules onto the machine that implements this LKM
* The rules are as follows:
* 	- DROP egress telnet packets
* 	- DROP ingress telnet packets
*	- DROP egress packets to restricted website (facebook.com)
* 	- DROP ingress ssh packets
*	- DROP egress ssh packets
* 
* Note to change facebook.com's IP address before running this script. 
*
* Author:      Wong Tin Kit
* Student ID : 1003331
*/

#include <linux/module.h> /* Needed by all modules */
#include <linux/kernel.h> /* Needed for KERN_INFO */
#include <linux/init.h>   /* Needed for the macros */
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/skbuff.h>

static struct nf_hook_ops nfho; 

unsigned int filter(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
	
	struct iphdr *iph;
	struct tcphdr *tcph;
	static unsigned char *ip_address = "\x80\xE6\x12\x3F"; //128.230.18.63 -> www.syr.edu
	iph = ip_hdr(skb);
	tcph = (void *)iph+iph->ihl*4;
	
	if (iph->protocol == IPPROTO_TCP && tcph->dest == htons(23)) 
	{
		printk(KERN_INFO "Dropping telnet packet to %d.%d.%d.%d\n",
		((unsigned char *)&iph->daddr)[0],
		((unsigned char *)&iph->daddr)[1],
		((unsigned char *)&iph->daddr)[2],
		((unsigned char *)&iph->daddr)[3]
		);
		return NF_DROP;
	}
	else if (iph->protocol == IPPROTO_TCP && tcph->source == htons(23))
	{
		printk(KERN_INFO "Dropping telnet packet from %d.%d.%d.%d\n",	
		((unsigned char *)&iph->saddr)[0],
		((unsigned char *)&iph->saddr)[1],
		((unsigned char *)&iph->saddr)[2],
		((unsigned char *)&iph->saddr)[3]
		);
		return NF_DROP;
	}
	else if (iph->saddr == *(unsigned int*)ip_address) 
	{
		printk(KERN_INFO "User accessing restricted site: www.syr.edu");
		return NF_DROP;
	}	
	else if (iph->protocol == IPPROTO_TCP && tcph->source == htons(22))
	{
		printk(KERN_INFO "Dropping ssh packet from %d.%d.%d.%d",
		((unsigned char *)&iph->saddr)[0],
		((unsigned char *)&iph->saddr)[1],
		((unsigned char *)&iph->saddr)[2],
		((unsigned char *)&iph->saddr)[3]
		);
		return NF_DROP;
	}
	else if (iph->protocol == IPPROTO_TCP && tcph->dest == htons(22))
	{
		printk(KERN_INFO "Dropping ssh packet to %d.%d.%d.%d",	
		((unsigned char *)&iph->daddr)[0],
		((unsigned char *)&iph->daddr)[1],
		((unsigned char *)&iph->daddr)[2],
		((unsigned char *)&iph->daddr)[3]
		);
		return NF_DROP;
	}
	else 
	{
		return NF_ACCEPT;
	}
}



int init_module(void)
{
	printk(KERN_INFO "Initialising Task2 filter\n");
	nfho.hook = filter;
	nfho.hooknum = NF_INET_PRE_ROUTING;
	nfho.pf = PF_INET;
	nfho.priority = NF_IP_PRI_FIRST;
	
	// Register hook
	nf_register_hook(&nfho);
	return 0;
}

void cleanup_module(void)
{
	printk(KERN_INFO "Task2 filter is being removed\n");
	nf_unregister_hook(&nfho);
}



